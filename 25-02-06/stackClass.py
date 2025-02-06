class StackArray():
    def __init__(self):
        self.stack = [None for _ in range(10)]
        self.STACK_FULL = len(self.stack) - 1
        self.top = -1

    def isFull(self):
        return self.top == self.STACK_FULL

    def isEmpty(self):
        return self.top == -1

    def pushStack(self, item):
        if self.top == self.STACK_FULL:
            print("Cannot push!")
        else:
            self.top += 1
            self.stack[self.top] = item

    def popStack(self):
        if self.top == -1:
            print("Stack Empty!")
        else:
            value = self.stack[self.top]
            self.top -= 1
            return value
