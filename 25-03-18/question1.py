# 1a)

class node:
    def __init__(self, data, nextNode):
        self.data = data # INTEGER
        self.nextNode = nextNode # INTEGER

# b)

linkedList = [
    node(1, 1),
    node(5, 4),
    node(6, 7),
    node(7, -1),
    node(2, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1)
] # OF node

startPointer = 0 # OF INTEGER
emptyList = 5 # OF INTEGER

# c)(i)

def outputNodes(node_array, start_pointer):
    next_node = node_array[start_pointer]
    print(next_node.data)
    while next_node.nextNode != -1:
        next_node = node_array[next_node.nextNode]
        print(next_node.data)

# (ii)

outputNodes(linkedList, startPointer)

# d)(i)

def addNode(node_array, start_pointer, free_pointer):
    global startPointer
    global emptyList
    data_to_add = int(input("Enter data: ")) # INTEGER

    if free_pointer == -1:
        return False
    
    last_element = start_pointer # INTEGER

    # Update the start_pointer
    start_pointer = free_pointer

    # Update the heap_pointer
    free_pointer = node_array[free_pointer].nextNode

    # Overwrite the old data
    node_array[start_pointer].data = data_to_add
    
    # Overwrite the old pointer
    node_array[start_pointer].nextNode = last_element

    startPointer = start_pointer
    emptyList = free_pointer

    return True

# (ii) & (iii)

if addNode(linkedList, startPointer, emptyList):
    print("Node successfully added")
else:
    print("linkedlist is full")
outputNodes(linkedList, startPointer)