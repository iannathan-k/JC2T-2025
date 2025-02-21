# 1a)

StackData = [None for _ in range(10)]
StackPointer = 0

# b)

def printStack():
    global StackPointer
    for data in StackData:
        print(data)
    print("StackPointer: ", str(StackPointer))

# c)

def Push(num_to_push):
    global StackPointer
    if StackPointer == len(StackData):
        return False
    
    StackData[StackPointer] = num_to_push
    StackPointer += 1
    return True

# d)(i) & (ii)

for i in range(11):
    user_num = input("Enter a number: ")

    if Push(user_num):
        print("Successfully added")
    else:
        print("Stack is full")

printStack()