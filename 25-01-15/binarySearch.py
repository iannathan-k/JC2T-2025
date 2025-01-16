array = [1, 2, 4, 8, 16, 32, 64, 128]

low = 0
high = len(array) - 1
search_element = int(input("Num to search?: "))
found = False
flag = True

while flag:
    mid  = (low + high) // 2
    if array[mid] == search_element:
        flag = False
        found = True
    elif search_element > array[mid]:
        low = mid + 1
    else:
        high = mid - 1

    if low > high:
        flag = False

if found:
    print("Found!")
else:
    print("Not Found")