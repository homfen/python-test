# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

range_num = 100
secret_number = 0
guess_num = 7


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,guess_num
    secret_number = random.randrange(0,range_num)
    print 'New game.Range is from 0 to',range_num
    if range_num==100:
        guess_num = 7
    else:
        guess_num = 10
    print 'Number of remaining guesses is',guess_num
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_num
    range_num = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_num
    range_num = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_num
    guess_num -= 1
    guess_input = int(guess)
    
    print 'Guess was',guess_input
    print 'Number of remaining guesses is',guess_num
    
    if secret_number==guess_input:
        print 'Correct!'
        print
        new_game()
    elif (secret_number > guess_input) and guess_num > 0:
        print 'Higher!'
        print
    elif (secret_number < guess_input) and guess_num > 0:
        print 'Lower!'
        print
    else:
        print 'You ran out of guesses. The number was',secret_number
        print
        new_game()

    
# create frame
f = simplegui.create_frame('Guess the number',200,200)

# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)',range100,200)
f.add_button('Range is [0, 1000)',range1000,200)
f.add_input('Enter a guess',input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric