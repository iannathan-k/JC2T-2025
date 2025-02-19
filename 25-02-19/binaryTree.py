tree =[[-1, i, -1] for i in range(1, 11)]
tree[9][1] = -1
root_pointer = -1
heap_pointer = 0

for line in tree:
    print(line)