#2a)

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] # OF INTEGER

# b)(i)

def linearSearch(search_element):
    for data in arrayData:
        if data == search_element: return True
    return False

# (ii)

num_to_find = int(input("Enter a number to search: "))
if linearSearch(num_to_find):
    print("Number was found")
else:
    print("Number not found")

# c)

def bubbleSort():
    swap = True
    top = len(arrayData) - 1
    while swap:
        swap = False
        for i in range(top):
            if arrayData[i] > arrayData[i + 1]: 
                swap = True
                arrayData[i], arrayData[i + 1] = arrayData[i + 1], arrayData[i]
        top -= 1