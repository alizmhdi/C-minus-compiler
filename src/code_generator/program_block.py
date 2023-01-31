class Instruction:
    def __init__(self, opcode, operand_1, operand_2, operand_3):
        self.opcode = opcode
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operand_3 = operand_3

    def __str__(self):
        return f'{self.opcode}, {self.operand_1}, {self.operand_2}, {self.operand_3}'

class ProgramBlock:
    def __init__(self):
        self.program_block = []

    def add_instruction(self, instruction: Instruction) -> None:
        self.program_block.append(instruction)

    def set_instruction(self, index: int, instruction: Instruction) -> None:
        self.program_block[index] = instruction

    def __str__(self) -> str:
        return '\n'.join([f'{i}\t{inst}' for i, inst in enumerate(self._instructions)])
