from writer.writer import Writer


class SyntaxErrorWriter(Writer):

    def __init__(self, file_name):
        super(SyntaxErrorWriter, self).__init__(file_name)

    def write(self, errors):
        if len(errors) == 0:
            result = 'There is no syntax error.'
        else:
            result = '\n'.join(errors)
        self.file.write(result)
        self.close_file()
