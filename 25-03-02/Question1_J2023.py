# 1a)(i)

DataArray = [None for _ in range(25)]

# (ii)
try:
    file = open("25-03-02/Data.txt", 'r')
    for i in range(25):
        DataArray[i] = int(file.readline().strip())
except FileNotFoundError:
    print("File was not found")

# b)(i)

def PrintArray(array):
    for item in array: 
        print(item, end=" ")
    print()

# (ii) & (iii)

PrintArray(DataArray)

# c)

def LinearSearch(array, search):
    total = 0
    for item in array:
        if item == search: total += 1

    return total

# d)(i) & (ii)

user_num = -1
while user_num not in range(101):
    user_num = int(input("Enter a number: "))

print(f"The number {user_num} was found {LinearSearch(DataArray, user_num)} times.")