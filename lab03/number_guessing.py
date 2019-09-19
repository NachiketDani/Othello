import random

def main():
    ## Generate random number between 1 and 50 for the game
    rand_num = random.randint(1,50)
    print (rand_num) ## COMMENT/DELETE LINE BEFORE YOU SUBMIT
    
    ## Initation of game and guess counter
    print ("Welcome to the Guessing Game!")
    guess1 = int((input ("I picked a number between 1 and 50. Try and guess!" "\n")))
    print("You guessed", guess1)
    guess_count = 1
    
    ## Initiate variable delta for calculating approach to answer
    delta = 1

    ## Determine clue to be provided and ask for next guess while incrementing guess count by 1
    while delta > 0:
        delta = abs(guess1-rand_num)
        if (delta == 1):
            guess1 = int (input ("Your guess is scalding hot \n"))
            guess_count += 1
        elif (delta == 2): 
            guess1 = int (input ("Your guess is extremely hot \n"))
            guess_count += 1
        elif (delta == 3):
            guess1 = int (input ("Your guess is very warm \n"))
            guess_count += 1
        elif (delta > 3 and abs(guess1-rand_num) <= 5):
            guess1 = int (input ("Your guess is warm \n"))
            guess_count += 1
        elif (delta > 5 and delta <= 8):
            guess1 = int (input ("Your guess is cold \n"))
            guess_count += 1
        elif (delta > 8 and delta <= 13):
            guess1 = int (input ("Your guess is very cold \n"))
            guess_count += 1
        elif (delta > 13 and delta <= 20):
            guess1 = int (input ("Your guess is extremely cold \n"))
            guess_count += 1
        elif (delta > 20):
            guess1 = int (input ("Your guess is icy freezing miserably cold \n"))
            guess_count += 1

    print ("Congratulations. You figured it out in", guess_count, "tries")
    if guess_count == 1:
        print ("That was lucky!")
    elif (guess_count >= 2 and guess_count <= 4):
        print ("That was amazing!")
    elif (guess_count >= 5 and guess_count <= 6):
        print ("That was okay.")
    elif (guess_count == 7):
        print ("Meh.")
    elif (guess_count == 8 or guess_count == 9):
        print ("This is not your game.")
    else:
        print ("You are the worst guesser I've ever seen.")

main()

