### Hangman

def hangman(word):
    wrong = 0
    picture = [
       "___________", # 0
       "|     |    ", # 1
       "|     O    ", # 2
       "|    /|\   ", # 3
       "|   / | \  ", # 4
       "|    / \   ", # 5
       "|  _/   \_ ", # 6
       "|__________"  # 7
       ]
    
    rletters = list(word) #[r, $, y, t, $ , m]
    board = ["_"] * len(word)  # [ r, h, y, t, h, m]
    win = False
    print("Welcome to Hangman!")
    print(" ".join(board))

    while win == False:
        message = "Guess a letter:"
        letter = input(message)

        if letter in rletters: # h
            while letter in rletters:
                index = rletters.index(letter) # 4
                board[index] = letter
                rletters[index] = "$"
            print(" ".join(board))
        else:
            wrong += 1
            print("\n".join(picture[0: wrong + 2]))
            print(" ".join(board))

        if "_" not in board:
            win = True
            print("Congratulations! You win!")

        if wrong > 5:
            print("Sorry you lost. The word was {}".format(word))
            break
            
            
            
            

hangman("rhythm")
