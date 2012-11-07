#!/usr/bin/python

import random
debug = False

def help():
    print "One Dimensional Space Fight"
    print "x - exit"
    print "q - quit"
    print "h - help"
    print "s - show"
    print "m - move"
    print "n - next game"
    print "d - debug"

def play():
    hidden = random.randrange(1, 201, 1)
    global debug

    while 1:
        if debug:
            print "Debug: ", hidden

        guess = raw_input("Guess: ")
        #print guess

        if guess == 'x' or guess == 'q':
            print "Thank you for playing"
            exit()

        if guess == 'h':
            help()
            continue

        if guess == 's':
            print "Secret: ", hidden
            continue

        if guess == 'n':
            print "Skipping this game "
            return

        if guess == 'd':
            debug = not debug
            continue

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

def run():
    help()
    while 1:
        play()

run()
