#!/usr/bin/python

import random

def play():
    hidden = random.randrange(1, 201, 1)
    print "Secret: ", hidden

    while 1:
        guess = raw_input("Guess: ")
        #print guess

        if guess == 'x':
            print "Thank you for playing"
            exit()

        try:
            guess = int(guess)

            if guess == hidden:
                print "Hit"
                break
            elif guess < hidden:
                print "guess is too small"
            else:
                print "guess is too high"

        except ValueError:
            print "Invalid input {:}".format(guess)


play()
