import math

def find_number(min_number, max_number, secret_number):
    guesses=0
    guess=max_number

    while(guess != secret_number):
        guess=math.floor(((max_number-min_number)/2) + min_number)
        print("Guessing %s..." %(guess,))
        guesses += 1
        if(guess > secret_number):
            print("Guessed too high")
            max_number=guess
        if(guess < secret_number):
            print("Guessed too low")
            min_number=guess

    print("Guessed %s in %s guesses" %(secret_number,guesses,))

find_number(0, 100, 11)
