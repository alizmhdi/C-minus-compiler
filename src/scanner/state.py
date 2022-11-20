states = {}


class State:
    def __init__(self, ID, is_final_state, is_star_state, state_type):
        self.id = ID
        self.is_final_state = is_final_state
        self.is_star_state = is_star_state
        self.type = state_type
        self.transitions = {}
        states[ID] = self

    @staticmethod
    def get_state_by_id(ID):
        return states[ID]

    def add_transition(self, dest_state, characters):
        for character in characters:
            self.transitions[character] = dest_state

    def get_dest_state_by_character(self, character):
        if character in self.transitions:
            return self.transitions[character]
