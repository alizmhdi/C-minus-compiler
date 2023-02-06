class SemanticStack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        self.top -= 1
        return self.stack.pop()

    def get_top(self, index=0):
        if self.top - index < 0:
            return None
        return self.stack[self.top - index]
