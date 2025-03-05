# 2 Types of OOP Variables
# 1. Instance Variable - (private) variables unique to each object
# 2. Class Variable - (static) variables which belong to every object

class Person:
    person_count = 0
    def __init__(self, name, dob, gender):
        self.__name = name # Instance Variables
        self.__dob = dob
        self.__gender = gender
        Person.person_count += 1 # Class Variable

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_gender(self):
        return self.__gender
    
    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob

    def set_gender(self, gender):
        self.__gender = gender

    def walk(self):
        print("The person is walking")

    def run(self):
        print("The person is running")

person1 = Person("Gopal", "December 28 1957", "Male")