array = [
    [12, 45, 76, 2],
    [23, 54, 67, 34],
    [62, 57, 43, 8]
]

def sort_array(arr):
    top = len(arr) - 1
    swap = True
    while swap:
        swap = False
        for i in range(top):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        top -= 1
    return arr

def binary_search(arr, search):
    top = len(arr) - 1
    bottom = 0
    
    while top >= bottom:
        mid = (top + bottom) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            top = mid - 1
        elif arr[mid] < search:
            bottom = mid + 1

    return -1

array = [sort_array(array[row]) for row in range(len(array))]

search_element = int(input("Value to search: "))
search_row = int(input("Row to search: "))

result = binary_search(array[search_row], search_element)
if result == -1:
    print("Not Found")
else:
    print("Found!")

print(array)