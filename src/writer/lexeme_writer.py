from writer.writer import Writer


class LexemeWriter(Writer):

    def __init__(self, file_name):
        super(LexemeWriter, self).__init__(file_name)

    def write(self, symbols):
        result = ''
        for s in symbols:
            result += f'{symbols.index(s) + 1}.\t{s}\n'
        self.file.write(result)
        self.close_file()
