from writer.writer import Writer


class ParseTreeWriter(Writer):

    def __init__(self, file_name):
        super(ParseTreeWriter, self).__init__(file_name)

    def write(self, parse_tree):
        self.file.write(parse_tree[:-1])
        self.close_file()




