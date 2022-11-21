from scanner.config import *


class Writer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.open_file()

    def open_file(self):
        self.file = open(self.filename, 'w')

    def close_file(self):
        self.file.close()

    def write_tokens_in_file(self, tokens):
        result = ''
        for token in tokens:
            if token[0] == WHITESPACE and token[1] == "\n":
                result += "\n"
            elif token[0] != WHITESPACE and token[0] != COMMENT:
                result += f'({token[0]}, {token[1]})'
        self.file.write(result)
        self.close_file()

    def write_lexical_errors_in_file(self, errors):
        result = ''
        for error in errors:
            result += f'({error[0]}, {error[1]})\n'
        self.file.write(result)
        self.close_file()

    def write_lexemes_in_file(self, symbols):
        result = ''
        for s in symbols:
            result += f'{s}\n'
        self.file.write(result)
        self.close_file()





