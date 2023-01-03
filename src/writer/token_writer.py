from writer.writer import Writer


class TokenWriter(Writer):

    def __init__(self, file_name):
        super(TokenWriter, self).__init__(file_name)

    def write(self, tokens):
        result = ''
        for i in tokens.keys():
            result += f'{i}.\t'
            for token in tokens[i]:
                result += f'({token[0]}, {token[1]}) '
            result += '\n'
        self.file.write(result)
        self.close_file()



