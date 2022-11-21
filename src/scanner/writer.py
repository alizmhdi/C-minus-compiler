class Writer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.open_file()

    def open_file(self):
        self.file = open(self.filename, 'w')

    def close_file(self):
        self.file.close()

    def write_in_file(self, items):
        result = ''
        for i in items.keys():
            result += f'{i}.\t'
            for token in items[i]:
                result += f'({token[0]}, {token[1]}) '
            result += '\n'

        self.file.write(result)
        self.close_file()

    def write_lexemes_in_file(self, symbols):
        result = ''
        for s in symbols:
            result += f'{s}\n'
        self.file.write(result)
        self.close_file()
