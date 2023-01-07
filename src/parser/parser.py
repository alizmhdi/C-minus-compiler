from scanner.config import *
from scanner.scanner import Scanner
import json
from anytree import Node, RenderTree


class Parser:

    def __init__(self):
        self.scanner = Scanner("input.txt")
        with open('./parser/grammar/table.json') as f:
            grammar_contents = f.read()
            f.close()
        grammar = json.loads(grammar_contents)
        self.terminal = grammar['terminals']
        self.non_terminal = grammar['non_terminals']
        self.first = grammar['first']
        self.follow = grammar['follow']
        self.grammar = grammar['grammar']
        self.parse_table = grammar['parse_table']
        self.stack = ['0']

    def get_next_token(self):
        current_token = self.scanner.get_next_token()

        while current_token and (current_token[0] == WHITESPACE or current_token[0] == COMMENT):
            current_token = self.scanner.get_next_token()

        return current_token

    def parse(self):
        current_token = self.get_next_token()
        while True:
            last_index = self.stack[-1]
            next_move = self.parse_table[last_index][Parser.get_token_value(current_token)].split('_')
            if next_move[0] == "accept":
                Node('$', left_rule_node)
                print(Parser.format_tree(left_rule_node))
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
                left_rule, right_rule = rule[0], rule[2:]
                left_rule_node = Node(left_rule)
                if right_rule != ['epsilon']:
                    start_reduce_index = len(self.stack) - 2 * len(right_rule)
                    for i in range(2 * len(right_rule)):
                        item = self.stack.pop(start_reduce_index)
                        if i % 2 == 0:
                            item.parent = left_rule_node
                next_move = self.parse_table[self.stack[-1]][left_rule].split('_')
                self.stack.append(left_rule_node)
                if next_move[0] != 'goto':
                    raise Exception("goto error")
                self.stack.append(next_move[1])

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
        if not token:
            return '$'
        if token[0] == KEYWORD or token[0] == SYMBOL:
            return token[1]
        return token[0]
