# 1a)

Animals = [None for _ in range(10)]

# b)

Animals = [
    "horse",
    "lion",
    "rabbit",
    "mouse",
    "bird",
    "deer",
    "whale",
    "elephant",
    "kangaroo",
    "tiger"
]

# c)

def SortDescending():
    ArrayLength = len(Animals)
    for X in range(ArrayLength):
        for Y in range(ArrayLength - X - 1):
            if (Animals[Y][0] < Animals[Y + 1][0]):
                Temp = Animals[Y]
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp

# d)(i) & (ii)

SortDescending()
for animal in Animals:
    print(animal)