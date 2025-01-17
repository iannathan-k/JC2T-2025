array = [
    [12, 45, 76, 2],
    [23, 54, 67, 34],
    [62, 57, 43, 8]
]

found = False
search_value = int(input("Enter a value: "))
search_row = int(input("Enter a row: "))
col = 0

while col < len(array[search_row]) and not found:
    if array[search_row][col] == search_value:
        found = True
        print("Found!")
        print("Column:", col)
    col += 1

if not found:
    print("Not Found")