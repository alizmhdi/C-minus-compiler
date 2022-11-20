from scanner.reader import Reader
from scanner.dfa import DFA
from scanner.state import states
from scanner.state import State


class Scanner:

    def __init__(self):
        self.reader = Reader("input.txt")
        DFA()
        self.start_state = states[0]
        self.current_state = self.start_state
        self.current_char = ""

    def get_next_token(self):
        token_name = ""

        while True:
            if self.current_state.id == 0 or (not self.current_state.is_star_state and not self.current_state.is_final_state):
                self.current_char = self.reader.read_char()
                self.current_state = self.next_state()
            elif self.current_state.is_star_state:
                self.current_state = self.start_state
                self.current_state = self.next_state()
            elif self.current_state.is_final_state:
                pass

    def next_state(self) -> State:
        pass
