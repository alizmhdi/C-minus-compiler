from scanner.config import *
from scanner.state import State


class DFA:
    def __init__(self):
        # error_state = State(-1, is_final_state=False, is_star_state=False, type=ERROR)
        state_0 = State(ID=0, is_final_state=False, is_star_state=False, state_type=START)

        # Number states
        state_1 = State(1, is_final_state=False, is_star_state=False, state_type=NUMBER)
        state_2 = State(2, is_final_state=True, is_star_state=True, state_type=NUMBER)

        # ID states
        state_3 = State(3, is_final_state=False, is_star_state=False, state_type=ID)
        state_4 = State(4, is_final_state=True, is_star_state=True, state_type=ID)

        # Symbol states
        state_5 = State(5, is_final_state=True, is_star_state=False, state_type=SYMBOL)
        state_6 = State(6, is_final_state=False, is_star_state=False, state_type=SYMBOL)
        state_7 = State(7, is_final_state=True, is_star_state=False, state_type=SYMBOL)
        state_8 = State(8, is_final_state=False, is_star_state=False, state_type=SYMBOL)
        state_9 = State(9, is_final_state=True, is_star_state=True, state_type=SYMBOL)

        # Comment states
        state_10 = State(10, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_11 = State(11, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_12 = State(12, is_final_state=True, is_star_state=False, state_type=COMMENT)
        state_13 = State(13, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_14 = State(14, is_final_state=True, is_star_state=False, state_type=COMMENT)

        # Whitespace state
        state_15 = State(15, is_final_state=True, is_star_state=False, state_type=WHITESPACE)

        # Number
        state_0.add_transition(state_1, digits)
        state_1.add_transition(state_1, digits)
        state_1.add_transition(state_2, all_symbols + whitespace)

        # Keyword and ID
        state_0.add_transition(state_3, letters)
        state_3.add_transition(state_3, letters + digits)
        state_3.add_transition(state_4, all_symbols + whitespace)

        # Whitespace
        state_0.add_transition(state_15, whitespace)

        # Symbol
        state_0.add_transition(state_5, symbol)
        state_0.add_transition(state_6, equal_symbol)
        state_6.add_transition(state_7, equal_symbol)
        state_6.add_transition(state_9, symbol + slash_symbol + star_symbol + whitespace + letters + digits)
        state_0.add_transition(state_8, slash_symbol)
        state_8.add_transition(state_9, symbol + equal_symbol + whitespace + letters + digits)

        # Comment
        state_8.add_transition(state_10, star_symbol)
        state_10.add_transition(state_10, symbol + equal_symbol + slash_symbol + whitespace + letters + digits)
        state_10.add_transition(state_11, star_symbol)
        state_11.add_transition(state_11, star_symbol)
        state_11.add_transition(state_10, symbol + equal_symbol + whitespace + letters + digits)
        state_11.add_transition(state_12, slash_symbol)
        state_8.add_transition(state_13, slash_symbol)
        state_13.add_transition(state_13, all_symbols + letters + digits + [' ', '\r', '\t', '\v', '\f'])
        state_13.add_transition(state_14, new_line)
