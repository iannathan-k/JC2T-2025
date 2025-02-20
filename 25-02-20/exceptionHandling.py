try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Q(x) =", num1 / num2)

    file = open("fileHandling.txt")

except ZeroDivisionError:
    print("Illegal division by zero")
except IndexError:
    print("Index out of bounds")
except FileNotFoundError:
    print("File was not found")