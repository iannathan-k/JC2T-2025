ll_data = [5, 6, 9, 3, None, None, None]
ll_pointers = [-1, 0, 1, 2, 5, 6, -1]
heap_pointer = 4
start_pointer = 3

def removeElement(num_to_remove):
    global start_pointer
    global heap_pointer

    i = start_pointer
    while i != -1:
        if ll_data[i] == num_to_remove: break
        previous_node = i
        i = ll_pointers[i]

    if i == start_pointer: previous_node = -1
    
    if (start_pointer == -1):
        print("Linked List Empty!")
        return
    if (i == -1):
        print("Item doesn't exist")
        return
    
    old_pointer = ll_pointers[i]
    
    # Remove Element
    ll_data[i] = None

    # Set pointer
    ll_pointers[i] = heap_pointer

    # Set previous pointer
    if previous_node == -1:
        start_pointer = old_pointer
    else:
        ll_pointers[previous_node] = old_pointer

    # Set pointers
    heap_pointer = i