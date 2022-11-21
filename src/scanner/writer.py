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
        for i in tokens.keys():
            result += f'{i}.\t'
            for token in tokens[i]:
                result += f'({token[0]}, {token[1]}) '
            result += '\n'
        self.file.write(result)
        self.close_file()

    def write_lexical_errors_in_file(self, errors):
        result = ''
        for i in errors.keys():
            result += f'{i}.\t'
            for error in errors[i]:
                if error[1] == 'Unclosed comment':
                    result += f'({error[0][0:6]} ..., {error[1]}) '
                else:
                    result += f'({error[0]}, {error[1]}) '
            result += '\n'

        if len(errors) == 0:
            result = 'There is no lexical error.'

        self.file.write(result)
        self.close_file()

    def write_lexemes_in_file(self, symbols):
        result = ''
        for s in symbols:
            result += f'{symbols.index(s)+1}.\t{s}\n'
        self.file.write(result)
        self.close_file()
