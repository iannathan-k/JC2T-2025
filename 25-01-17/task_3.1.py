# Part 1

array = [
    [12, 45, 76, 2],
    [23, 54, 67, 34],
    [62, 57, 43, 8]
]

found = False
search_value = int(input("Enter a value: "))
row = 0

while row < len(array) and not found:
    for col in range(len(array[row])):
        if array[row][col] == search_value:
            found = True
            print("Found!")
            print("Row:", row)
            print("Column:", col)
    row += 1

if not found:
    print("Not Found")

# Part 3

