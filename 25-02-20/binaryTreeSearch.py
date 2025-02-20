tree = [
    [1,   9,  2],
    [3,   7, -1],
    [4,  13,  5],
    [-1,  5, -1],
    [-1, 12, -1],
    [-1, 15, -1],
    [-1,  7, -1],
    [-1,  8, -1],
    [-1,  9, -1],
    [-1, -1,- 1]
]

root_pointer = 0
heap_pointer = 6

def searchTree(value):
    global root_pointer
    current_index = root_pointer

    while current_index != -1:
        current_node = tree[current_index]
        if current_node[1] == value:
            return current_index   
        elif value < current_node[1]:
            current_index = current_node[0]
        else:
            current_index = current_node[2]

    return -1