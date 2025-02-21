# 1a)

score_board = [[None, None] for _ in range(11)]

# b)

def ReadHighScores():
    try:

        file = open("25-02-20/question1_mj22_41/HighScore.txt", "r")
        for i in range(10):
            score_board[i][0] = file.readline().strip()
            score_board[i][1] = int(file.readline().strip())
        file.close()

    except FileNotFoundError:
        print("File was not found!")

# c)

def OutputHighScores():
    for entry in score_board:
        print(entry[0], str(entry[1]))

# d)(i) & (ii)

ReadHighScores()
OutputHighScores()

# e)(i)

player_name = ""
player_score = -1

while len(player_name) != 3:
    player_name = input("Enter a valid character name: ")

while player_score > 100000 or player_score < 1:
    player_score = int(input("Enter a valid player score: "))

# (ii)

def MakeNewTopTen(player_name, player_score):
    score_board[10] = [player_name, player_score]
    for i in range(9, 0, -1):
        if score_board[i][1] < player_score:
            score_board[i], score_board[i + 1] = score_board[i + 1], score_board[i]
        else:
            break

# (iii) & (iv)

MakeNewTopTen(player_name, player_score)
OutputHighScores()

# f)

def WriteTopTen():
    file = open("25-02-20/question1_mj22_41/NewHighScore.txt", "w")
    for entry in score_board[:10]:
        file.write(entry[0] + "\n")
        file.write(str(entry[1]) + "\n")
    file.close()