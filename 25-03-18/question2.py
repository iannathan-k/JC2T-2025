# 2a)

arrayData = [15, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# b) (i)

def linearSearch(num_to_find):
    for num in arrayData:
        if num == num_to_find: return True
    return False

# (ii) & (iii)

num = int(input("Enter a num to find: "))
if linearSearch(num):
    print("Number was found")
else:
    print("Number was not found")

# c)

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - x - 1):
            if (arrayData[y] > arrayData[y + 1]):
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp