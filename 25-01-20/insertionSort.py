array = [2, 67, 31, 78, 213, 6, 4, 8, 3]
print(array)

for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while key < array[j] and j >= 0:
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp
        j -= 1

print(array)