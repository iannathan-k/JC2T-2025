# ll_data = [None for _ in range(10)]
# ll_pointers = [None for _ in range(10)]
# heap_pointer = 0
# start_pointer = -1

# for i in range(len(ll_pointers)):
#     ll_pointers[i] = i + 1
# ll_pointers[len(ll_pointers) - 1] = -1

ll_data = [5, 6, 9, 3, None, None, None]
ll_pointers = [-1, 0, 1, 2, 5, 6, -1]
heap_pointer = 4
start_pointer = 3

i = start_pointer
while i != -1:
    print(ll_data[i])
    i = ll_pointers[i]

print(ll_data)
print(ll_pointers)