class TemporariesBlock:
    def __init__(self):
        self.temporaries = {}
        self.last_index = 3000

    def get_temp(self):
        self.last_index += 1
        return self.last_index

    def set_type(self, address, typ):
        self.temporaries[address] = typ

    def get_type(self, address):
        return 'var', 'int'
