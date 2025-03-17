# 1a)

DataStored = [None for _ in range(20)] # OF INTEGER
NumberItems = 0 # INTEGER

# b)

def Initialise():
    global NumberItems
    num_to_enter = -1
    while num_to_enter not in range(1, 21):
        num_to_enter = int(input("Number of Items: "))
    
    NumberItems = num_to_enter
    for i in range(num_to_enter):
        DataStored[i] = int(input("Enter next num: "))

# c)(i) & (ii)

NumberItems = 0
Initialise()
print(DataStored)

# d) (i)

def BubbleSort():
    flag = True # BOOLEAN
    top = NumberItems - 1 # INTEGER
    while flag:
        flag = False
        for i in range(top):
            if DataStored[i] > DataStored[i + 1]:
                DataStored[i], DataStored[i + 1] = DataStored[i + 1], DataStored[i]
                flag = True
        top -= 1

# (ii) & (iii)

BubbleSort()
print(DataStored)

# e)(i)

def BinarySearch(DataToFind):
    bottom = 0 # INTEGER
    top = NumberItems - 1 # INTEGER
    while bottom <= top:
        mid = (bottom + top) // 2
        item = DataStored[mid]

        if item == DataToFind: return mid
        if DataToFind > item: bottom = mid + 1
        if DataToFind < item: top = mid - 1
    
    return -1

# (ii)

num_to_find = int(input("Enter a num to find: "))
print(BinarySearch(num_to_find))