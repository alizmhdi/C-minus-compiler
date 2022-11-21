from scanner.config import *


class SymbolTable:

    def __init__(self):
        self.lexemes = keywords.copy()

    def add_lexeme(self, lexeme):
        if lexeme not in self.lexemes:
            self.lexemes.append(lexeme)


symbol_table = SymbolTable()

