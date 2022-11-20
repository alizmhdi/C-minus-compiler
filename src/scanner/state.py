states = {}

class State:
    def __init__(self, ID, is_final_state, is_star_state ,type):
        self.ID = ID
        self.is_final_state = is_final_state
        self.is_star_state = is_star_state
        self.type = type
        self.transitions = {}
        states[id] = self

    @staticmethod
    def get_state_by_id(id):
        return states[id]

    def add_transition(self, dest_state, characters):
        for character in characters:
            self.transitions[character] = dest_state

    def get_dest_state_by_character(self, character):
        if character not in self.transitions:
            raise
        return self.transitions[character]
