from scanner.config import *
from scanner.state import State, states


class DFA:
    def __init__(self):
        state_0 = State(ID=0, is_final_state=False, is_star_state=False, state_type=START)
        eof_state = State(ID=-5, is_final_state=False, is_star_state=False, state_type=EOF)
        invalid_input_error_state = State(-1, is_final_state=False, is_star_state=False, state_type=ERROR, error_message="Invalid input")
        unmatched_comment_error_state = State(-2, is_final_state=False, is_star_state=False, state_type=ERROR, error_message="Unmatched comment")
        unclosed_comment_error_state = State(-3, is_final_state=False, is_star_state=False, state_type=ERROR, error_message="Unclosed comment")
        invalid_number_error_state = State(-4, is_final_state=False, is_star_state=False, state_type=ERROR, error_message="Invalid number")

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
        state_16 = State(16, is_final_state=False, is_star_state=False, state_type=SYMBOL)

        # Comment states
        state_10 = State(10, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_11 = State(11, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_12 = State(12, is_final_state=True, is_star_state=False, state_type=COMMENT)
        state_13 = State(13, is_final_state=False, is_star_state=False, state_type=COMMENT)
        state_14 = State(14, is_final_state=True, is_star_state=False, state_type=COMMENT)

        # Whitespace state
        state_15 = State(15, is_final_state=True, is_star_state=False, state_type=WHITESPACE)

        # Start -> Start (by empty String)
        state_0.add_transition(state_0, [""])

        # Number
        state_0.add_transition(state_1, digits)
        state_1.add_transition(state_1, digits)
        state_1.add_transition(state_2, all_symbols + whitespace)
        state_1.add_transition(invalid_number_error_state, letters)

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
        state_0.add_transition(state_16, star_symbol)
        state_16.add_transition(state_9, symbol + star_symbol + equal_symbol + whitespace + letters + digits)
        state_16.add_transition(unmatched_comment_error_state, slash_symbol)

        # Comment
        state_8.add_transition(state_10, star_symbol)
        state_10.add_transition(state_10, get_all_chars(['*']))
        state_10.add_transition(state_11, star_symbol)
        state_11.add_transition(state_11, star_symbol)
        state_11.add_transition(state_10, symbol + equal_symbol + whitespace + letters + digits)
        state_11.add_transition(state_12, slash_symbol)
        state_8.add_transition(state_13, slash_symbol)
        state_13.add_transition(state_13, get_all_chars(['\n']))
        state_13.add_transition(state_14, new_line)
        state_10.add_transition(unclosed_comment_error_state, [''])

        DFA.set_invalid_input_state_transition(invalid_input_error_state, [state_13, state_10])
        DFA.add_eof_transition(eof_state, [state_10])

    @staticmethod
    def set_invalid_input_state_transition(error_state, exceptions):
        for state in states.values():
            if not state.is_final_state and state not in exceptions:
                state.add_transition(error_state, invalid_chars)

    @staticmethod
    def add_eof_transition(eof_state, exceptions):
        for state in states.values():
            if state not in exceptions:
                state.add_transition(eof_state, [''])
