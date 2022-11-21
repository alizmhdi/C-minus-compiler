from scanner.scanner import Scanner
from scanner.writer import Writer
from scanner.dfa import DFA
from scanner.symbol_table import symbol_table
from scanner.config import *

if __name__ == '__main__':
    DFA()
    scanner = Scanner("input.txt")

    tokens = {}
    while True:
        current_token = scanner.get_next_token()
        if not current_token:
            break
        token_line = current_token[2]
        if current_token[0] == WHITESPACE or current_token[0] == COMMENT:
            continue
        if token_line not in tokens:
            tokens[token_line] = [current_token]
        else:
            tokens[token_line].append(current_token)

    Writer("./tokens.txt").write_tokens_in_file(tokens)
    Writer("./lexical_errors.txt").write_lexical_errors_in_file(scanner.lexical_errors)
    Writer("./symbol_table.txt").write_lexemes_in_file(symbol_table.lexemes)
