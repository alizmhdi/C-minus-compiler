class Data:
    def __init__(self, lexeme, typ, address, scope):
        self.num_args = None
        self.keyword = None
        self.lexeme = lexeme
        self.address = address
        self.scope = scope
        self.type = typ
        self.params = []
        self.line = 0
        self.return_value_address = 0
        self.return_address = 0

    def set_keyword(self, keyword):
        if self.type == 'void' and keyword != 'func':
            raise Exception(f"Illegal type of void for '{self.lexeme}'.")
            return
        self.keyword = keyword

    def set_num_args(self, num_args):
        self.num_args = num_args

    def add_param(self, param: int):
        self.params.append(param)

    def add_type(self, typ):
        self.type = typ

    def set_line(self, line: int):
        self.line = line

    def set_return_value_addr(self, address):
        self.return_value_address = address

    def set_return_addr(self, address):
        self.return_address = address

    def __str__(self):
        return f'lexeme: {self.lexeme},\t address: {self.address},\t keyword: {self.keyword},\t type: {self.type},\t num_args: {self.num_args},\t scope: {self.scope},\t params: {self.params}'


class DataBlock:
    def __init__(self):
        initial_data = Data('output', 'int', 0, 0)
        self.all_data = [initial_data]
        self.last_index = 2000
        self.scope_stack = [0]
        self.max_scope = 0

    def get_data(self, lexeme: str):
        scope = self.all_data[self.scope_stack[-1]].scope
        for data in self.all_data:
            if data.lexeme == lexeme and (data.scope == scope or data.keyword == 'func' or data.scope == 0 or
                                          (data.keyword == 'param' and data.scope == 0)):
                return data, None

        # print(f'Variable {lexeme} not declared')
        return self.all_data[0], f"'{lexeme}' is not defined."

    def create_data(self, lexeme: str, typ: str):
        scope = self.all_data[self.scope_stack[-1]].scope
        data = Data(lexeme, typ, self.last_index, scope)
        self.all_data.append(data)
        self.last_index += 4
        return data

    def increase_index(self, size: int):
        self.last_index += 4 * int(size)

    def get_data_from_address(self, address: int):
        for data in self.all_data:
            if data.address == address:
                return data

    def get_data_from_index(self, index: int):
        return self.all_data[index]

    def add_virtual_row(self):
        data = Data('virtual', '', None, self.max_scope + 1)
        self.max_scope += 1
        self.scope_stack.append(len(self.all_data))
        self.all_data.append(data)

    def end_scope(self):
        self.scope_stack.pop()

    def __str__(self):
        return ''.join('\n'.join(f'{it}: {str(data)}' for it, data in enumerate(self.all_data)))
