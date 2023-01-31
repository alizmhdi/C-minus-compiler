from src.code_generator.semantic_stack import SemanticStack
from src.code_generator.program_block import ProgramBlock

class CodeGenerator:
    def __init__(self):
        self.semantic_stack = SemanticStack()
        self.program_block = ProgramBlock
