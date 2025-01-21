# 2(a)
from random import *

ArrayData = [[randint(1, 100) for _ in range(10)] for _ in range(10)]

# (b)(ii)
def printArray():
    for row in ArrayData:
        for col in row:
            print(col, end=" ")
        print()

# (b)(i)
if __name__ == "__main__":

    ArrayLength = 10
    for x in range(ArrayLength - 1):
        for y in range(ArrayLength - 2):
            for z in range(ArrayLength - y - 2):
                if ArrayData[x][z] > ArrayData[x][z + 1]:
                    TempValue = ArrayData[x][z]
                    ArrayData[x][z] = ArrayData[x][z + 1]
                    ArrayData[x][z + 1] = TempValue