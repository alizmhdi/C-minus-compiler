class Reader:

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.open_file()
        self.current_line = ""
        self.current_line_number = 0
        self.index = 0
        self.read_line()

    def open_file(self):
        self.file = open(self.filename, 'r')

    def read_line(self):
        self.current_line = self.file.readline()
        self.current_line_number += 1
        self.index = 0

    def read_char(self):
        if self.current_line == '':
            self.file.close()
            return ''
        elif self.index >= len(self.current_line):
            self.read_line()
            return self.read_char()
        else:
            result = self.current_line[self.index]
            self.index += 1
            return result

    def get_current_line_number(self):
        return self.current_line_number

    def close_file(self):
        self.file.close()
