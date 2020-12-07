while True:
    try:
        guessNum = int(input("Guess a number between 1 and 10: "))
        if guessNum == 7:
            print("You guessed it")
            break
        else:
            print("Sorry, please try again.")
    except ValueError:
        print("You didn't input a number between 1 and 10")
    except:
        print("Unknown error")

