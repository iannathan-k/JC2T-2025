# 3a)(i)

class Device:
    def __init__(self, device_name, brand, battery_life, price):
        self.__device_name = device_name # STRING
        self.__brand = brand # STRING
        self.__battery_life = battery_life # INTEGER
        self.__price = price # FLOAT

    def get_device_name(self):
        return self.__device_name
    
    def get_brand(self):
        return self.__brand
    
    def get_battery_life(self):
        return self.__battery_life
    
    def get_price(self):
        return self.__price
    
    def print_details(self):
        print(f"Name: {self.__device_name}, Brand: {self.__brand}, Battery Life: {self.__battery_life}, Price: {self.__price}")

# (ii)

class Phone(Device):
    def __init__(self, device_name, brand, battery_life, price, storage):
        super().__init__(device_name, brand, battery_life, price)
        self.__storage = storage # INTEGER

    def get_storage(self):
        return self.__storage
    
    def print_details(self):
        print(f"Name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Storage: {self.get_storage()}")

# (iii)

class Laptop(Device):
    def __init__(self, device_name, brand, battery_life, price, ram):
        super().__init__(device_name, brand, battery_life, price)
        self.__ram = ram # INTEGER

    def get_ram(self):
        return self.__ram
    
    def print_details(self):
        print(f"Name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Ram: {self.get_ram()}")

class Tablet(Device):
    def __init__(self, device_name, brand, battery_life, price, screen_size):
        super().__init__(device_name, brand, battery_life, price)
        self.__screen_size = screen_size # FLOAT

    def get_screen_size(self):
        return self.__screen_size
    
    def print_details(self):
         print(f"Name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Screen Size: {self.get_screen_size()}")

# b)

def ReadDeviceData():
    device_array = [] # OF Device

    try:
        file = open("Devices.txt", 'r')

        device_line = file.readline().strip() # STRING

        while device_line != "":
            device_info = device_line.split(",") # OF STRING

            if device_info[0] == "Phone":
                device_array.append(Phone(device_info[1], device_info[2], int(device_info[3]), float(device_info[4]), int(device_info[5])))
            elif device_info[0] == "Laptop":
                device_array.append(Laptop(device_info[1], device_info[2], int(device_info[3]), float(device_info[4]), int(device_info[5])))
            else:
                device_array.append(Tablet(device_info[1], device_info[2], int(device_info[3]), float(device_info[4]), float(device_info[5])))

            device_line = file.readline().strip()

        file.close()

    except FileNotFoundError:
        print("File not found")
         
    return device_array

# c)

def PrintDevices(device_array):
    for device in device_array:
        device.print_details()

# d)(i) & (ii)

device_array = ReadDeviceData() # OF Device
PrintDevices(device_array)

# e(i)

def ChooseDevice(device_array):
    try:
        budget = float(input("Enter a budget: ")) # FLOAT
        brand = input("Enter a preffered brand: ") # STRING
        battery = int(input("Enter a minimum battery life: ")) # INTEGER
    except ValueError:
        print("Invalid Number")
        
    matching_array = [] # OF Device

    for device in device_array:
        if device.get_price() > budget: continue
        if device.get_brand() != brand: continue
        if device.get_battery_life() < battery: continue

        matching_array.append(device)

    return matching_array

# (ii)

choice_array = ChooseDevice(device_array) # OF Device
if len(choice_array) == 0: print("No available devices")
else: PrintDevices(choice_array)

