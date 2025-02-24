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

def insertToTree(value):
    global root_pointer
    global heap_pointer
    if heap_pointer == -1:
        print("Tree is full!")
        return

    new_item_pointer = heap_pointer

    # change the heap pointer location
    heap_pointer = tree[heap_pointer][1]

    # find the node to change
    current_node = None
    current_index = root_pointer
    while current_index != -1:
        current_node = tree[current_index]
        if value < current_node[1]:
            side = True
            current_index = current_node[0]
        elif value > current_node[1]:
            side = False
            current_index = current_node[2]

    # change the pointer of the parent node
    if root_pointer == -1:
        root_pointer = new_item_pointer
    elif side:
        current_node[0] = new_item_pointer
    else:
        current_node[2] = new_item_pointer

    # add the value to the location
    tree[new_item_pointer][1] = value 