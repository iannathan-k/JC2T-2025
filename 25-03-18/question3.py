# 3a)

class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question # STRING
        self.__answer = answer # INTEGER
        self.__points = points # INTEGER

    # c)(i)

    def getQuestion(self):
        return self.__question
    
    # (ii)

    def checkAnswer(self, user_answer):
        return user_answer == self.__answer
    
    # (iii)

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0

# b)

arrayTreasure = [] # OF TreasureChest

def readData():
    try:
        file = open("25-03-18/TreasureChestData.txt")

        for i in range(5):
            question = file.readline().strip() # STRING
            answer = int(file.readline().strip()) # INTEGER
            points = int(file.readline().strip()) # INTEGER
            arrayTreasure.append(TreasureChest(question, answer, points))
        
    except FileNotFoundError:
        print("File not found")

# c)(iv)

readData()
question_no = int(input("Enter a question to be ask: "))
print(arrayTreasure[question_no].getQuestion())
attempt_count = 0
user_answer = None
while not arrayTreasure[question_no].checkAnswer(user_answer):
    user_answer = int(input("Enter your answer: "))
    attempt_count += 1
print(arrayTreasure[question_no].getPoints(attempt_count))