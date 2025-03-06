class Person:
    person_count = 0
    def __init__(self, name, dob, gender):
        self.__name = name # Instance Variables
        self.__dob = dob
        self.__gender = gender
        Person.person_count += 1 # Class Variable

    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob
    
    def getGender(self):
        return self.__gender
    
    def setName(self, name):
        self.__name = name

    def setDob(self, dob):
        self.__dob = dob

    def setGender(self, gender):
        self.__gender = gender

    def printDetails(self):
        print(f"{self.__name}, {self.__gender} born {self.__dob}")

    def walk(self):
        print("The person is walking")

    def run(self):
        print("The person is running")

class Teacher(Person):
    def __init__(self, name, dob, gender, salary):
        super().__init__(name, dob, gender)
        self.__salary = salary
    
    def printDetails(self):
        print(f"{self.getName()}, {self.getGender()} born {self.getDob()} earning {self.__salary}")

class Student(Person):
    def __init__(self, name, dob, gender, grade):
        super().__init__(name, dob, gender)
        self.__grade = grade

    def printDetails(self):
        print(f"{self.getName()}, {self.getGender()} born {self.getDob()} scoring {self.__grade}")

person1 = Teacher("Gopal", "December 28 1957", "Male", "infinite")
person2 = Student("Ian", "July 5 2008", "Male", "A*")
person1.printDetails()
person2.printDetails()