from scanner.scanner import Scanner
from writer.token_writer import *
from writer.error_writer import *
from writer.lexeme_writer import *
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

    TokenWriter("./tokens.txt").write(tokens)
    ErrorWriter("./lexical_error.txt").write(scanner.lexical_errors)
    LexemeWriter("./symbol_table.txt").write(symbol_table.lexemes)
