ll_data = [5, 6, 9, 3, None, None, None]
ll_pointers = [-1, 0, 1, 2, 5, 6, -1]
heap_pointer = 4
start_pointer = 3

def findElement(num_to_find):
    i = start_pointer
    while i != -1:
        if ll_data[i] == num_to_find: return i
        i = ll_pointers[i]
    return -1