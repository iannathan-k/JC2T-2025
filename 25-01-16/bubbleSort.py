array = [2, 67, 31, 78, 213, 6, 4, 8, 3]
top = len(array) - 1
swap = True

while swap:
    swap = False
    for i in range(top):
        if array[i] > array[i + 1]:
            swap = True
            temp = array[i + 1]
            array[i + 1] = array[i]
            array[i] = temp

    top -= 1