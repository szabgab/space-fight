#!/usr/bin/python

import random
debug = False
move = False
N = 200

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
    hidden = random.randrange(1, N+1, 1)
    global debug
    global move

    while 1:
        if debug:
            print "Debug: ", hidden
        if move:
            hidden = hidden + random.randrange(-2, 3, 1)
            if hidden < 1:
                hidden = 1
            if hidden > N:
                hidden = N

        guess = raw_input("Guess: ")

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

        if guess == 'm':
            move = not move
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
