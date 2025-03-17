# 2a)

import random

ArrayData = [[random.randint(1, 100) for i in range(10)] for j in range(10)]

# b)(i)

ArrayLength = 10
for X in range(ArrayLength):
    for Y in range(ArrayLength - 1):
        for Z in range(ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z + 1]
                ArrayData[X][Z + 1] = TempValue

# (ii) & (iii)

def PrintArray():
    for row in ArrayData:
        for col in row:
            print(col, end=" ")
        print()

PrintArray()

# c) (i) & (ii)

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper > Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if (SearchArray[0][Mid] > SearchValue):
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1

print(BinarySearch(ArrayData, 0, len(ArrayData), int(input("Enter a num: "))))
print(BinarySearch(ArrayData, 0, len(ArrayData), int(input("Enter a num: "))))