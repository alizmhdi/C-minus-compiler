from writer.writer import Writer


class CodeGeneratorWriter(Writer):

    def __init__(self, file_name):
        super(CodeGeneratorWriter, self).__init__(file_name)

    def write(self, program_block):
        result = str(program_block)
        self.file.write(result)
        self.close_file()




