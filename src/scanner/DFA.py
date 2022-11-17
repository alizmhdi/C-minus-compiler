from src.scanner.config import *
from src.scanner.state import State


def initial_DFA():
    state_0 = State(0, is_accept_state=False, is_star_state=False, type=START)

    state_1 = State(1, is_accept_state=False, is_star_state=False, type=NUMBER)
    state_2 = State(2, is_accept_state=True, is_star_state=True, type=NUMBER)

    state_3 = State(3, is_accept_state=False, is_star_state=False, type=ID)
    state_4 = State(4, is_accept_state=True, is_star_state=True, type=ID)

    state_5 = State(5, is_accept_state=True, is_star_state=False, type=SYMBOL)
    state_6 = State(6, is_accept_state=False, is_star_state=False, type=SYMBOL)
    state_7 = State(7, is_accept_state=True, is_star_state=False, type=SYMBOL)
    state_8 = State(8, is_accept_state=False, is_star_state=False, type=SYMBOL)
    state_9 = State(9, is_accept_state=True, is_star_state=True, type=SYMBOL)

    state_10 = State(10, is_accept_state=False, is_star_state=False, type=COMMENT)
    state_11 = State(11, is_accept_state=False, is_star_state=False, type=COMMENT)
    state_12 = State(12, is_accept_state=True, is_star_state=False, type=COMMENT)
    state_13 = State(13, is_accept_state=False, is_star_state=False, type=COMMENT)
    state_14 = State(14, is_accept_state=False, is_star_state=False, type=COMMENT)

    state_15 = State(15, is_accept_state=True, is_star_state=False, type=WHITESPACE)
    #numner
    state_0.add_transition(state_1, digits)
    state_1.add_transition(state_1, digits)
    state_1.add_transition(state_2, symbol + whitespace)
    #keyword and id
    state_0.add_transition(state_3, letters)
    state_3.add_transition(state_3, letters + digits)
    state_3.add_transition(state_4, symbol + whitespace)
    #whitespace
    state_0.add_transition(state_15, whitespace)
    #symbol
    #comment

