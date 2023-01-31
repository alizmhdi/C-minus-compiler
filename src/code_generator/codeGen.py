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

    def variable_declaration(self):
        address = self.semantic_stack.pop()
        instruction = Instruction('ASSIGN', '#0', address, ' ')
        self.program_block.add_instruction(instruction)

    def array_declaration(self):
        size = self.semantic_stack.pop()
        self.variable_declaration()
        self.data_block.increase_index(size)

    def save(self):
        self.program_block.increase_index()
        self.semantic_stack.push(self.program_block.last_index)

    def push_type(self, token):
        self.semantic_stack.push(token)

    def add(self):
        pass






