# 2a)(i)

class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName # STRING
        self.__HeightGrowth = HeightGrowth # INTEGER
        self.__MaxHeight = MaxHeight # INTEGER
        self.__MaxWidth = MaxWidth # INTEGER
        self.__Evergreen = Evergreen # STRING

    # (ii)

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight
    
    def GetMaxWidth(self):
        return self.__MaxWidth
    
    def GetEvergreen(self):
        return self.__Evergreen
    
# b)

def ReadData():
    TreeArray = [] # OF Tree

    try:
        file = open("25-03-13/Trees.txt")

        for i in range(9):
            tree_line = file.readline().strip().split(",")
            TreeArray.append(Tree(tree_line[0], int(tree_line[1]), int(tree_line[2]), int(tree_line[3]), tree_line[4]))
    except FileNotFoundError:
        print("File does not exist")

    return TreeArray

# c)

def PrintTrees(tree_obj):
    if tree_obj.GetEvergreen() == "Yes":
        print(f"{tree_obj.GetTreeName()} has a maximum height {tree_obj.GetMaxHeight()} a maximum width {tree_obj.GetMaxWidth()} and grows {tree_obj.GetGrowth()} cm a year. It does not lose its leaves.")
    else:
        print(f"{tree_obj.GetTreeName()} has a maximum height {tree_obj.GetMaxHeight()} a maximum width {tree_obj.GetMaxWidth()} and grows {tree_obj.GetGrowth()} cm a year. It loses its leaves each year.")

# d)(i) & (ii)

trees = ReadData()
PrintTrees(trees[0])

# e)

def ChooseTree(tree_array):
    maxheight = int(input("Enter a max height: "))
    maxwidth = int(input("Enter a max width: "))
    evergreen = input("Evergreen or not: ")

    for tree in tree_array:
        if tree.GetMaxHeight() > maxheight: continue
        if tree.GetMaxWidth() > maxwidth: continue
        if tree.GetEvergreen() != evergreen: continue

        