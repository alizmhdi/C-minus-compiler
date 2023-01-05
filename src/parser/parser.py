from scanner.config import *
from scanner.scanner import Scanner
import json
from anytree import RenderTree, Node


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
        self.nodes = {}

    def get_next_token(self):
        current_token = self.scanner.get_next_token()

        while current_token and (current_token[0] == WHITESPACE or current_token[0] == COMMENT):
            current_token = self.scanner.get_next_token()

        return current_token

    def parse(self):
        current_token = self.get_next_token()
        self.create_node(current_token)
        while True:
            last_index = self.stack[-1]
            next_move = self.parse_table[last_index][Parser.get_token_value(current_token)].split('_')
            if next_move[0] == "accept":
                print("Accept")
                return
            elif next_move[0] == 'shift':
                self.stack.append(current_token)
                self.stack.append(next_move[1])
                current_token = self.get_next_token()
                self.create_node(current_token)
            elif next_move[0] == 'reduce':
                rule = self.grammar[next_move[1]]
                left_rule, right_rule = rule[0], rule[2:]
                if right_rule != ['epsilon']:
                    for _ in range(2 * len(right_rule)):
                        self.stack.pop()
                next_move = self.parse_table[self.stack[-1]][left_rule].split('_')
                self.stack.append(left_rule)
                if next_move[0] != 'goto':
                    raise Exception("goto error")
                self.stack.append(next_move[1])

    def create_node(self, token):
        token_value = Parser.get_token_value(token)
        node = Node(token_value)
        self.nodes[token] = token_value

    @staticmethod
    def get_token_value(token):
        if not token:
            return '$'
        if token[0] == KEYWORD or token[0] == SYMBOL:
            return token[1]
        return token[0]
