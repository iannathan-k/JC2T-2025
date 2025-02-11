ll_data = [5, 6, 9, 3, None, None, None]
ll_pointers = [-1, 0, 1, 2, 5, 6, -1]
heap_pointer = 4
start_pointer = 3

def addElement(num_to_add):
    global heap_pointer
    global start_pointer
    if heap_pointer == -1:
        print("Linked List Full!")
        return
    
    last_element = start_pointer

    # Update the start_pointer
    start_pointer = heap_pointer

    # Update the heap_pointer
    heap_pointer = ll_pointers[heap_pointer]

    # Overwrite the old data
    ll_data[start_pointer] = num_to_add
    
    # Overwrite the old pointer
    ll_pointers[start_pointer] = last_element