#CHAPTER 10

#Hangman

def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|          |        ",
              "|          0        ",
              "|         /|\       ",
              "|         / \       ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("you lose! It was {}.".format(word))

# hangman("cat")
            
# 1. Modify the game so that a word is selected randomly from a list of words.
import random

listOfWords = ["word", "dog", "blue", "pink"]
index = random.randrange(4)
hangman(listOfWords[index])



