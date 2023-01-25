from scanner.reader import Reader
from scanner.state import states
from scanner.state import State
from scanner.symbol_table import symbol_table
from scanner.config import *


class Scanner:

    def __init__(self, input_file):
        self.reader = Reader(input_file)
        self.start_state = states[0]
        self.current_char = ''
        self.lexical_errors = {}

    def get_next_token(self):
        current_state = self.start_state
        token_name = ""

        while True:
            if current_state.id == 0 or (not current_state.is_star_state and not current_state.is_final_state):
                self.current_char = self.reader.read_char()
                current_state = self.next_state(current_state)
                if current_state.type == ERROR:
                    error = (token_name + self.current_char, current_state.error_message)
                    error_line = self.find_start_line(self.reader.current_line_number, error[0])
                    if error_line not in self.lexical_errors:
                        self.lexical_errors[error_line] = [error]
                    else:
                        self.lexical_errors[error_line].append(error)
                    token_name = ""
                    continue
                if not self.current_char:
                    return EOF, '$', self.reader.current_line_number
                if current_state == self.start_state:
                    self.reader.index -= 1
                    token_name = ""
                    continue
                if current_state.is_star_state:
                    self.reader.index -= 1
                    if current_state.type == ID:
                        symbol_table.add_lexeme(token_name)
                    if token_name in keywords:
                        return KEYWORD, token_name, self.reader.current_line_number
                    return current_state.type, token_name, self.reader.current_line_number
                elif current_state.is_final_state:
                    token_name += self.current_char
                    return current_state.type, token_name, self.reader.current_line_number
                token_name += self.current_char

    def next_state(self, current_state: State) -> State:
        next_state = current_state.get_dest_state_by_character(self.current_char)
        if next_state:
            return next_state
        return self.start_state

    @staticmethod
    def find_start_line(current_line, message):
        return current_line - message.count('\n')
