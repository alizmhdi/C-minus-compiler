class SemanticStack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.top <= 0:
            return None
        return self.stack.pop()

    def get_top(self, index = 0):
        return self.stack[self.top - index]