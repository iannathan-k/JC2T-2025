# 2a)

Data = [[None for _ in range(4)] for __ in range(5)]
Rows = 5

# b)

def SetUp():
    global Rows
    try:
        row_num = -1
        while row_num < 1 or row_num > 5:
            row_num = int(input("No. of rows: "))

        Rows = row_num
        for i in range(row_num):
            for j in range(4):
                Data[i][j] = int(input("Enter data: "))

    except ValueError:
        print("Invalid Number")

# c)(i) & (ii)

SetUp()
# for row in Data:
#     print(row)

# d)(i)

def BubbleSort():
    for k in range(Rows):
        row = Data[k] # OF INTEGER
        for i in range(4):
            for j in range(3):
                if row[j] > row[j + 1]:
                    temp = row[j] # INTEGER
                    row[j] = row[j + 1]
                    row[j + 1] = temp

# (ii) & (iii)

BubbleSort()
# for row in Data:
#     print(row)

# e)(i)

def RecursiveBinarySearch(row_num, DataToFind, low, high):
    if low > high: return -1

    mid = (low + high) // 2 # INTEGER
    if Data[row_num][mid] == DataToFind: return mid
    if Data[row_num][mid] > DataToFind: return RecursiveBinarySearch(row_num, DataToFind, low, mid - 1)
    if Data[row_num][mid] < DataToFind: return RecursiveBinarySearch(row_num, DataToFind, mid + 1, high)

# (ii) & (iii) & (iv)

try:
    search_row_num = int(input("Enter a row to search: ")) # INTEGER
    data_to_find = int(input("Enter a data to find: ")) # INTEGER

    result = RecursiveBinarySearch(search_row_num - 1, data_to_find, 0, 3) # INTEGER
    if result == -1: print("Number not found.")
    else: print(f"Number found at column {result + 1} in row {search_row_num}")

except ValueError:
    print("Invalid Number")