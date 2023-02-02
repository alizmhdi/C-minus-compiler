class DataBlock:
    def __init__(self):
        self.data = {}
        self.last_index = 2000

    def get_address(self, symbol: str):
        if symbol not in self.data.keys():
            self.data[symbol] = self.last_index
            self.last_index += 4
        return self.data[symbol]

    def get_value(self, address: int):
        return self.data[address]

    def increase_index(self, size: int):
        self.last_index += 4 * int(size)
