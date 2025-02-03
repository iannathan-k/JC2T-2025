stack = [None for _ in range(10)]
STACK_FULL = len(stack) - 1
top = -1

def pushStack(item):
    global top
    if len(stack) == STACK_FULL:
        print("Cannot push!")
    else:
        top += 1
        stack[top] = item

def popStack():
    global top
    if top == -1:
        print("Stack Empty!")
        return -1
    else:
        value = stack[top]
        top -= 1
        return value
