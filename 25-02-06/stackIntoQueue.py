import stackClass

stack_a = stackClass.StackArray()
stack_b = stackClass.StackArray()

def transferStack(stack1, stack2):
    while not stack1.isEmpty():
        stack2.pushStack(stack1.popStack())
    
def pushQueue(item):
    transferStack(stack_a, stack_b)
    stack_a.pushStack(item)
    transferStack(stack_b, stack_a)

def popQueue():
    return stack_a.popStack()
