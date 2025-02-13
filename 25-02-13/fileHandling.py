file = open("25-02-13/Numbers.txt", 'r')
number_array =[int(file.readline().strip()) for _ in range(10)]
print(number_array)