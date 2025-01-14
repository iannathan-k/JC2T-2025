array = ['a', 'b', 'c']

toFind = input("Item to find?: ")
flag = False


for item in array:
    if item == toFind:
        flag = True

if flag:
    print("Item Found!")
else:
    print("Not Found")