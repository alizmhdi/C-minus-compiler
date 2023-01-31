class TemporariesBlock:
    def __init__(self):
        self.temporaries = {}
        self.last_index = 3000

    def get_temp(self):
        self.last_index += 1
        return self.last_index

    def set_value(self, address, value):
        self.temporaries[address] = value

    def get_value(self, address):
        return self.temporaries[address]
