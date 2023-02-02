from scanner.config import *
from scanner.scanner import Scanner
from anytree import Node, RenderTree
from writer.syntax_error_writer import SyntaxErrorWriter
from writer.parse_tree_writer import ParseTreeWriter
from code_generator.code_gen import CodeGenerator
import json


with open('parser/grammar/table.json', 'r') as f:
    grammar = json.load(f)
    f.close()

semantic_actions = ["PID", "PNUM", "PTYPE", "FUNC", "VAR_DEC", "ARRAY_DEC", "BREAK_JP", "SAVE", "JPF", "JPF_SAVE", "JP",
                    "WHILE", "LABEL_WHILE", "LABEL_SWITCH", "ASSIGN", "ARRAY_CELL", "RELOP", "ADDOP", "MULTOP"]


class Parser:

    def __init__(self):
        self.scanner = Scanner("input.txt")
        self.terminal = grammar['terminals']
        self.non_terminal = grammar['non_terminals']
        self.first = grammar['first']
        self.follow = grammar['follow']
        self.grammar = grammar['grammar']
        self.parse_table = grammar['parse_table']
        self.stack = ['0']
        self.gotos = self.goto_states()
        self.errors = []
        self.syntax_error_writer = SyntaxErrorWriter('syntax_errors.txt')
        self.parse_tree_writer = ParseTreeWriter('parse_tree.txt')
        self.code_generator = CodeGenerator()

    def get_next_token(self):
        current_token = self.scanner.get_next_token()

        while current_token and (current_token[0] == WHITESPACE or current_token[0] == COMMENT):
            current_token = self.scanner.get_next_token()

        return current_token

    def parse(self):
        current_token = self.get_next_token()
        while True:
            last_index = self.stack[-1]
            try:
                next_move = self.parse_table[last_index][Parser.get_token_value(current_token)].split('_')
            except Exception:
                self.errors.append(f"#{current_token[2]} : syntax error , illegal {Parser.get_token_value(current_token)}")
                current_token = self.get_next_token()
                while self.stack[-1] not in self.gotos:
                    self.stack.pop()
                    removed = self.stack.pop()
                    if removed.name in self.non_terminal:
                        self.errors.append(f"syntax error , discarded {removed.name} from stack")
                    else:
                        self.errors.append(f"syntax error , discarded ({removed.name[0]}, {removed.name[1]}) from stack")
                while not self.is_in_follows(self.stack[-1], Parser.get_token_value(current_token)):
                    if Parser.get_token_value(current_token) == '$':
                        self.errors.append(f"#{current_token[2]} : syntax error , Unexpected EOF")
                        self.syntax_error_writer.write(self.errors)
                        return
                    self.errors.append(f"#{current_token[2]} : syntax error , discarded {current_token[1]} from input")
                    current_token = self.get_next_token()
                next_non_terminal = self.is_in_follows(self.stack[-1], Parser.get_token_value(current_token))
                next_state = self.parse_table[self.stack[-1]][next_non_terminal].split('_')[1]
                self.errors.append(f"#{current_token[2]} : syntax error , missing {next_non_terminal}")
                self.stack.append(Node(next_non_terminal))
                self.stack.append(next_state)

                continue
            if next_move[0] == "accept":
                Node('$', left_rule_node)
                self.parse_tree_writer.write(Parser.format_tree(left_rule_node))
                self.syntax_error_writer.write(self.errors)
                print(len(self.code_generator.program_block.instructions))
                print(self.code_generator.program_block)
                return
            elif next_move[0] == 'shift':
                if current_token:
                    node = Node((current_token[0], current_token[1]))
                else:
                    node = Node(current_token)
                self.stack.append(node)
                self.stack.append(next_move[1])
                current_token = self.get_next_token()
            elif next_move[0] == 'reduce':
                rule = self.grammar[next_move[1]]
                function = self.code_generator.function_dict.get(int(next_move[1]))
                if function:
                    if int(next_move[1]) in [68, 69, 70, 71, 81]:
                        function(current_token[1])
                    else:
                        function()
                left_rule, right_rule = rule[0], rule[2:]
                left_rule_node = Node(left_rule)
                if right_rule != ['epsilon']:
                    start_reduce_index = len(self.stack) - 2 * len(right_rule)
                    for i in range(2 * len(right_rule)):
                        item = self.stack.pop(start_reduce_index)
                        if i % 2 == 0:
                            item.parent = left_rule_node
                else:
                    Node('epsilon', left_rule_node)
                next_move = self.parse_table[self.stack[-1]][left_rule].split('_')
                self.stack.append(left_rule_node)
                if next_move[0] != 'goto':
                    raise Exception("goto error")
                self.stack.append(next_move[1])

    def goto_states(self) -> list:
        result = []

        for state in self.parse_table.keys():
            row = self.parse_table[state]
            for word in row.values():
                if word.startswith('goto'):
                    result.append(state)
                    break

        return result

    def get_gotos_alphabetically(self, state: str):
        result = []
        state_row = self.parse_table[state]
        for word in state_row.keys():
            if state_row[word].startswith('goto'):
                result.append(word)
        result.sort()
        return result

    def is_in_follows(self, state: str, token):
        gotos = self.get_gotos_alphabetically(state)
        for goto in gotos:
            if token in self.follow[goto]:
                return goto

        return None

    @staticmethod
    def format_tree(root: Node):
        result = ''
        for pre, fill, node in RenderTree(root):
            result += '%s%s' % (pre, Parser.format_node_name(node)) + '\n'
        return result

    @staticmethod
    def format_node_name(node):
        if type(node.name) == tuple:
            return f'({node.name[0]}, {node.name[1]})'
        return node.name

    @staticmethod
    def get_token_value(token):
        if token[0] == EOF:
            return '$'
        if token[0] == KEYWORD or token[0] == SYMBOL:
            return token[1]
        return token[0]
