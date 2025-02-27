# sum of all elements in an array with recursion
def sumOfArray(array):
    if len(array) == 0: return 0
    return array[0] + sumOfArray(array[1:])

def reverseString(string):
    if len(string) == 0: return ""
    return string[-1] + reverseString(string[:-1])

# Count occurences of any given character
def countCharacters(string, char):
    if len(string) == 0: return 0

    if string[0] == char:
        return 1 + countCharacters(string[1:], char)
    else:
        return countCharacters(string[1:], char)

def fibbonaci(num):
    if num <= 1: return num
    return fibbonaci(num - 1) + fibbonaci(num - 2)

# def fibbonaci(num):
#     if num == 0: return 1
#     print(num)
#     return num + fibbonaci(num - 1)

def binarySearch(array, lower_bound, upper_bound, num):
    if upper_bound < lower_bound: return -1

    mid = (lower_bound + upper_bound) // 2
    if num == array[mid]: return mid
    if num > array[mid]: return binarySearch(array, mid + 1, upper_bound, num)
    if num < array[mid]: return binarySearch(array, lower_bound, mid - 1, num)

print(sumOfArray([1, 2, 3, 4, 5]))
print(reverseString("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(countCharacters("Hello World", 'l'))
print(fibbonaci(3))
print(binarySearch([1, 4, 7, 9, 10, 12], 0, 5, 123))

# 1 1 2 3 5 8 13
for i in range(10):
    print(fibbonaci(i))