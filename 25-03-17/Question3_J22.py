# 3a)

class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number # INTEGER
        self.__Colour = Colour # STRING
    
    # b)
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    

# c)

CardArray = [Card(-1, "") for _ in range(30)] # OF CARD

try:
    file = open("25-03-17/CardValues.txt", 'r')

    for i in range(30):
        CardNumber = int(file.readline().strip()) # INTEGER
        CardColour = file.readline().strip() # STRING
        CardArray[i] = Card(CardNumber, CardColour)
except FileNotFoundError:
    print("File not found")

# d)

ChosenCards = []

def ChooseCard():
    PlayerCard = -1 # INTEGER
    while PlayerCard not in range(1, 31) or PlayerCard in ChosenCards:
        PlayerCard = int(input("Enter an index: "))
        
    ChosenCards.append(PlayerCard)
    return PlayerCard - 1

# e)(i) & (ii)
Player1 = [] # OF CARD
for i in range(4):
    index = ChooseCard()
    Player1.append(CardArray[index])

for card in Player1:
    print(f"Number: {card.GetNumber()}, Colour: {card.GetColour()}")