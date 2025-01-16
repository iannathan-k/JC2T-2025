array = [2, 67, 31, 78, 213, 6, 4, 8, 3]

total = 0
highest = array[0]
lowest = array[0]

for i in range(len(array)):
    total += array[i]
    
    if array[i] > highest:
        highest = array[i]
    if array[i] < lowest:
        lowest = array[i]

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)