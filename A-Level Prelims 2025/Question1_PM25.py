# 1a)

BeverageQueue = [None for _ in range(10)] # OF STRING
BeverageFrontPointer = 0 # INTEGER
BeverageRearPointer = 0 # INTEGER

# b)(i)

def DisplayMenu():
    try:
        file = open("BeverageData.txt", 'r')
        beverage = file.readline().strip()
        while beverage != "":
            print(beverage)
            beverage = file.readline().strip()
    except FileNotFoundError:
        print("File not found")
    file.close()

# (ii)

def TakeOrder():
    menu_array = [] # OF STRING
    try:
        file = open("BeverageData.txt", 'r')
        beverage = file.readline().strip().lower()
        while beverage != "":
            menu_array.append(beverage)
            beverage = file.readline().strip().lower()
    except FileNotFoundError:
        print("File not found")
    file.close()

    try:
        file = open("Order.txt", 'w')

        customer_order = input() # STRING
        order_array = customer_order.split(',') # OF STRING

        for order in order_array:
            order = order.strip()
            if order.lower() in menu_array:
                file.write(order + "\n")

    except FileExistsError:
        print("File already exists")
    file.close()

# (iii)

def EnqueueBeverage(DataToEnqueue):
    global BeverageRearPointer
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer = BeverageRearPointer + 1
        return True
    
# (iv)

def ReadOrderData():
    try:
        file = open("Order.txt", 'r')
        next_line = file.readline().strip() # STRING
        while next_line != "":
            EnqueueBeverage(next_line)
            next_line = file.readline().strip()

    except FileNotFoundError:
        print("File not found")

# c)(i)

def DequeueBeverage():
    global BeverageFrontPointer
    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer] # STRING
        BeverageFrontPointer = BeverageFrontPointer + 1
        return ReturnData
    
# (ii)

def ServeItem():
    beverage = DequeueBeverage() # STRING
    if beverage == "":
        print("No more orders to serve")
    else:
        print("You ordered", beverage)

# d)(i)

DisplayMenu()
TakeOrder()
ReadOrderData()
for i in range(BeverageRearPointer - BeverageFrontPointer):
    ServeItem()