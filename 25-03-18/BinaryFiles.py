import pickle

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
student1 = Student("Ian", 16)
    
file = open("25-03-18/Students.dat", "wb") # wb = write binary
pickle.dump(student1, file)
file.close()

file = open("25-03-18/Students.dat", "rb") # rb = read binary
student = pickle.load(file)
file.close()

print(student.getName())
print(student.getAge())