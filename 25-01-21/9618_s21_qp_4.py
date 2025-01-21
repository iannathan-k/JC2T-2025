# 2(a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] # OF INTEGER

# (b)(i)
def linearSearch(num):
    for data in arrayData:
        if data == num:
            return True
    else:
        return False
    
# (b)(ii)
user_num = int(input("Enter num to find: "))
if linearSearch(user_num):
    print("Number found")
else:
    print("Number not found")

# (c)
theArray = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] # OF INTEGER

def bubbleSort():
    for x in range(len(theArray) - 1):
        for y in range(len(theArray)):
            if theArray[y] < theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp