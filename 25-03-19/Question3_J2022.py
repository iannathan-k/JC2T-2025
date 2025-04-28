# 3a)(i)

class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay # REAL
        self.__EmployeeNumber = EmployeeNumber # STRING
        self.__JobTitle = JobTitle # STRING
        self.__PayYear2022 = [0.0 for _ in range(52)] # OF REAL

    # (ii)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    # (iii)

    def SetPay(self, week_no, hour_no):
        self.__PayYear2022[week_no - 1] = hour_no * self.__HourlyPay # INTEGER

    # (iv)

    def GetTotalPay(self):
        total = 0 # INTEGER
        for pay in self.__PayYear2022:
            total += pay
        return total

# b)(i)

class Manager(Employee):
    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle):
        self.__BonusValue = BonusValue # REAL
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)

    # (ii)

    def SetPay(self, week_no, hour_no):
        return super().SetPay(week_no, hour_no * (1 + self.__BonusValue / 100))
    
# c)

EmployeeArray = [None for _ in range(8)]
try:
    file = open("25-03-19/Employees.txt")

    for i in range(8):
        hourpay = float(file.readline().strip())
        employeenum = file.readline().strip()
        bonusortitle = file.readline().strip()

        try:
            bonus = float(bonusortitle)
            title = file.readline().strip()
            EmployeeArray[i] = Manager(bonus, hourpay, employeenum, title)
        except:
            title = bonusortitle
            EmployeeArray[i] = Employee(hourpay, employeenum, title)

    file.close()
except FileNotFoundError:
    print("File not found")

# d)

def EnterHours():
    try:
        file = open("25-03-19/HoursWeek1.txt", 'r')
        for i in range(8):
            employee_num = file.readline().strip()
            hours = float(file.readline().strip())
            
            for j in range(8):
                if EmployeeArray[j].GetEmployeeNumber() == employee_num:
                    EmployeeArray[j].SetPay(1, hours)
                    break
            
    except:
        print("File not found")

# e)(i) & (ii)

EnterHours()
for employee in EmployeeArray:
    employee_id = employee.GetEmployeeNumber()
    print(f"{employee.GetEmployeeNumber()}: {employee.GetTotalPay()}")