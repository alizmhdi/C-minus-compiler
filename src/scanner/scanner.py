from scanner.reader import Reader
from scanner.dfa import DFA
from scanner.state import states
from scanner.state import State


class Scanner:

    def __init__(self, input_file):
        self.reader = Reader(input_file)
        DFA()
        self.start_state = states[0]
        self.current_char = ''

    def get_next_token(self):
        current_state = self.start_state
        token_name = ""

        while True:
            if current_state.id == 0 or (not current_state.is_star_state and not current_state.is_final_state):
                self.current_char = self.reader.read_char()
                current_state = self.next_state(current_state)
                if current_state.is_star_state:
                    self.reader.index -= 1
                    return current_state.type, token_name
                elif current_state.is_final_state:
                    token_name += self.current_char
                    return current_state.type, token_name
                token_name += self.current_char

    def next_state(self, current_state: State) -> State:
        return current_state.get_dest_state_by_character(self.current_char)
