# 3a)(i)

class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__HourlyPay = HourlyPay # REAL
        self.__EmployeeNumber = EmployeeNumber # STRING
        self.__JobTitle = JobTitle # STRING
        self.__PayYear2022 = PayYear2022 # OF REAL
    

    # (ii)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    # (iii)

    def SetPay(self, week_no, hour_no, ):
        self.__PayYear2022[week_no] = hour_no * self.__HourlyPay # INTEGER

    # (iv)

    def GetTotalPay(self):
        total = 0 # INTEGER
        for pay in self.__PayYear2022:
            total += pay
        return total

# b)(i)

class Manager(Employee):
    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__BonusValue = BonusValue # REAL
        super().__init__(HourlyPay, EmployeeNumber, JobTitle, PayYear2022)

    # (ii)

    def SetPay(self, week_no, hour_no):
        return super().SetPay(week_no, hour_no + self.__BonusValue)
    
# c)

EmployeeArray = [None for _ in range(8)]
try:
    file = open("25-03-19/Employees.txt")

    for i in range(8):
        hourpay = float(file.readline().strip())
        employeenum = file.readline().strip()
        bonus = float(file.readline().strip())
        jobtitle = file.readline().strip()

        EmployeeArray[i] = 

except FileNotFoundError:
    print("File not found")

