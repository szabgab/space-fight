#!/usr/bin/python

import random

hidden = random.randrange(1, 201, 1)
print "Secret: ", hidden

guess = raw_input("Guess: ")
print guess

if guess == 'x':
    print "Thank you for playing"
    exit()

try:
    guess = int(guess)

    if guess == hidden:
        print "Hit"
    elif guess < hidden:
        print "guess is too small"
    else:
        print "guess is too high"

except ValueError:
    print "Invalid input {:}".format(guess)

