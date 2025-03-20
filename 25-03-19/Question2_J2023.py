# 2a)

class SaleData:
    def __init__(self, ID, quantity):
        self.ID = ID # STRING
        self.quantity = quantity # INTEGER

# b)

CircularQueue = [SaleData("", -1) for _ in range(5)] # OF SaleData

Head = 0
Tail = 0
NumberOfItems = 0

# c)

def Enqueue(sale_record):
    global NumberOfItems
    global Tail
    if NumberOfItems == 5:
        return -1

    CircularQueue[Tail] = sale_record
    if Tail == 4:
        Tail = 0
    else:
        Tail += 1
        
    NumberOfItems += 1
    return 1

# d)

def Dequeue():
    global NumberOfItems
    global Head
    if NumberOfItems == 0:
        return None
    
    record = CircularQueue[Head]
    NumberOfItems -= 1
    if Head == 4:
        Head = 0
    else:
        Head += 1

    return record

# e)

def EnterRecord():
    ID = input("Enter an id: ")
    Quantity = int(input("Enter a quantity: "))

    if Enqueue(SaleData(ID, Quantity)) == -1:
        print("Full")
    else:
        print("Stored")

# f)(i)

for i in range(6):
    EnterRecord()

record = Dequeue()
if (record == None):
    print("Queue is empty!")
else:
    print(record.ID)

EnterRecord()

for record in CircularQueue:
    print(record.ID, record.quantity)