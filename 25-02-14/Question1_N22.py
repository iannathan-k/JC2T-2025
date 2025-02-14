# 1a)

DataArray = [None for _ in range(100)]

# b)

def ReadFile():
    try:
        file = open("25-02-14/IntegerData.txt", 'r')
        for i in range(100):
            line = int(file.readline().strip())
            DataArray[i] = line
    except IOError:
        print("File not found")
    except ValueError:
        print("Invalid number")
    except:
        print("An error occured")

# c)

def FindValues():
    num_to_find = -1
    while num_to_find not in range(101):
        num_to_find = int(input("Enter a search value: "))

    count = 0
    for num in DataArray:
        if num == num_to_find: 
            count += 1
    return count

# d)(i)

ReadFile()
print(f"Your number was found: {FindValues()} times")

# e)

def BubbleSort():
    sorted = False
    top = 99
    while not sorted and top > 0:
        sorted = True
        for i in range(top):
            if DataArray[i] > DataArray[i + 1]:
                sorted = False
                temp = DataArray[i]
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = temp
        top -= 1

    print(DataArray)

BubbleSort()