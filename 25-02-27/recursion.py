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
    if num <= 0: return 1
    return fibbonaci(num - 1) + fibbonaci(num - 2)

def fibbonaci(num):
    if num == 0: return 1
    return num + fibbonaci(num - 1)

print(sumOfArray([1, 2, 3, 4, 5]))
print(reverseString("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(countCharacters("Hello World", 'l'))
print(fibbonaci(3))