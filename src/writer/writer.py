class Writer:

    def __init__(self, file_name):
        self.file = None
        self.file_name = file_name
        self.open_file()

    def open_file(self):
        self.file = open(self.file_name, 'w')

    def close_file(self):
        self.file.close()

    def write(self, data):
        raise NotImplementedError()

