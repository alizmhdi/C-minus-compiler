from code_generator.semantic_stack import SemanticStack
from code_generator.program_block import ProgramBlock, Instruction
from code_generator.data_block import DataBlock
from code_generator.temporaries_block import TemporariesBlock


class CodeGenerator:
    def __init__(self):
        self.semantic_stack = SemanticStack()
        self.program_block = ProgramBlock()
        self.data_block = DataBlock()
        self.temporaries = TemporariesBlock()

    def pid(self, lexeme):
        address = self.data_block.get_address(lexeme)
        self.semantic_stack.push(address)

    def assign(self):
        value = self.semantic_stack.pop()
        address = self.semantic_stack.pop()
        instruction = Instruction('ASSIGN', value, address, ' ')
        self.program_block.add_instruction(instruction)

    def variable_declaration(self):
        address = self.semantic_stack.pop()
        instruction = Instruction('ASSIGN', '#0', address, ' ')
        self.program_block.add_instruction(instruction)

    def array_declaration(self):
        size = self.semantic_stack.pop()
        self.variable_declaration()
        self.data_block.increase_index(size)

    def save(self):
        self.semantic_stack.push(self.program_block.last_index)
        self.program_block.increase_index()

    def push(self, token):
        self.semantic_stack.push(token)

    def add(self):
        op_1 = self.semantic_stack.pop()
        operator = self.semantic_stack.pop()
        op_2 = self.semantic_stack.pop()
        t = self.temporaries.get_temp()
        if operator == '+':
            instruction = Instruction('ADD', op_1, op_2, t)
        else:
            instruction = Instruction('SUB', op_1, op_2, t)
        self.program_block.add_instruction(instruction)

    def mult(self):
        op_1 = self.semantic_stack.pop()
        operator = self.semantic_stack.pop()
        op_2 = self.semantic_stack.pop()
        t = self.temporaries.get_temp()
        instruction = None
        if operator == '*':
            instruction = Instruction('MULT', op_1, op_2, t)
        elif operator == '/':
            instruction = Instruction('DIV', op_1, op_2, t)
        self.program_block.add_instruction(instruction)

    def func(self):
        pass

    def jp(self):
        address = self.semantic_stack.pop()
        instruction = Instruction('JP', address, ' ', ' ')
        self.program_block.add_instruction(instruction)

    def jpf(self):
        address = self.semantic_stack.pop()
        condition = self.semantic_stack.pop()
        instruction = Instruction('JPF', condition, address, ' ')
        self.program_block.add_instruction(instruction)

    def relop(self):
        op_1 = self.semantic_stack.pop()
        operator = self.semantic_stack.pop()
        op_2 = self.semantic_stack.pop()
        t = self.temporaries.get_temp()
        instruction = None
        if operator == '<':
            instruction = Instruction('LT', op_1, op_2, t)
        elif operator == '==':
            instruction = Instruction('EQ', op_1, op_2, t)
        self.program_block.add_instruction(instruction)

    def jpf_save(self):
        instruction_address = self.semantic_stack.pop()
        instruction = Instruction('JPF', self.semantic_stack.pop(), self.program_block.last_index + 1, ' ')
        self.program_block.set_instruction(instruction_address, instruction)
        self.program_block.increase_index()
        self.semantic_stack.push(self.program_block.last_index)

    def label_while(self):
        self.semantic_stack.push(self.program_block.last_index)
        self.program_block.increase_index()
        temp = self.temporaries.get_temp()
        self.semantic_stack.push(temp)
        self.semantic_stack.push(self.program_block.last_index)

    def while_end(self):
        address_to_jpf = self.semantic_stack.pop()
        expression = self.semantic_stack.pop()
        end_of_while_address = self.program_block.last_index + 1
        instruction = Instruction('JPF', expression, end_of_while_address, ' ')
        self.program_block.set_instruction(address_to_jpf, instruction)

        address_to_jp = self.semantic_stack.pop()
        instruction = Instruction('JP', address_to_jp, ' ', ' ')
        self.program_block.add_instruction(instruction)

        temp_address = self.semantic_stack.pop()
        instruction = Instruction('ASSIGN', end_of_while_address, temp_address, ' ')
        self.program_block.set_instruction(self.semantic_stack.pop(), instruction)

    def break_while(self):
        instruction = Instruction('JP', f'@{self.semantic_stack.get_top(3)}', ' ', ' ')
        self.program_block.add_instruction(instruction)

    def array_cell(self):
        index = self.semantic_stack.pop()
        address = self.semantic_stack.pop()
        temp = self.temporaries.get_temp()
        instruction = Instruction('ASSIGN', address + 4 * index, temp, ' ')
        self.program_block.add_instruction(instruction)
        self.semantic_stack.push(temp)

