# 2a)

class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description # OF TYPE STRING
        self.__Width = Width # OF TYPE INTEGER
        self.__Height = Height # OF TYPE INTEGER
        self.__FrameColour = FrameColour # OF TYPE STRING

    # b)
    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height
    
    def GetWidth(self):
        return self.__Width
    
    def GetColour(self):
        return self.__FrameColour
    
    # c)
    def SetDescription(self, Description):
        self.__Description = Description

# d)

picture_array = [None for _ in range(100)] # OF TYPE Picture

# e)

def ReadData():
    try:
        file = open("25-03-06/Pictures.txt")
        index = 0
        while True:
            description = file.readline().strip()

            if description == "": return index

            width = int(file.readline().strip())
            height = int(file.readline().strip())
            color = file.readline().strip()

            picture_array[index] = Picture(description, width, height, color)
            index += 1
    except FileNotFoundError:
        print("File was not found")

# f)

ReadData()

# g)

frame_color = input("Enter picture color: ")
max_width = int(input("Enter picture width: "))
max_height = int(input("Enter picture height: "))

for picture in picture_array:
    if picture == None: break
    if picture.GetColour().lower() != frame_color.lower(): continue
    if picture.GetWidth() > max_width: continue
    if picture.GetHeight() > max_height: continue

    print("Description: " + picture.GetDescription())
    print("Width: " + str(picture.GetWidth()))
    print("Height: " + str(picture.GetHeight()))