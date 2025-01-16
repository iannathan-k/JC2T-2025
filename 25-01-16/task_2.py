array = [
    [12, 45, 76, 2],
    [23, 45, 76, 34],
    [62, 57, 43, 8]
]

column_totals = [0 for row in array[0]]
column_high = [0 for row in array[0]]
highest_row = 0

for i in range(len(array)):
    row_total = 0
    row_high = array[i][0]
    for j in range(len(array[i])):
        row_total += array[i][j]
        if array[i][j] > row_high:
            row_high = array[i][j]
        
        column_totals[j] += array[i][j]
        if array[i][j] > column_high[j]:
            column_high[j] = array[i][j]

    print("Row Total:", row_total)
    print("Row High:", row_high)

print("Column Totals:", str(column_totals))
print("Column Highs:", str(column_high))