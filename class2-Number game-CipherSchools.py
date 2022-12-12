
winning_number = 43
guess = 1# how many times user guessed
number = int(input("guess a number between 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you win,you guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("two low")
            guess+=1
            number = int(input("guess again: "))
        else:
            print("Too high")
            guess+=1
            number = int(input("Guess again: "))    
          


