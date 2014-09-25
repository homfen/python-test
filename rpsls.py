# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        return 100

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        return "rock"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # print out the message for the player's choice
    if player_number>4:
        print "Invalid choice"
        return
        
    print "Player chooses ",player_choice

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses ",comp_choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message
    tie = "Player and computer tie!"
    playWin = "Player wins!"
    compWin = "Computer wins!"

    if player_number==comp_number:
        print tie
    elif player_number==0 and (comp_number==3 or comp_number==4):
        print playWin
    elif player_number==1 and (comp_number==0 or comp_number==4):
        print playWin
    elif player_number==2 and (comp_number==0 or comp_number==1):
        print playWin
    elif player_number==3 and (comp_number==1 or comp_number==2):
        print playWin
    elif player_number==4 and (comp_number==2 or comp_number==3):
        print playWin
    elif comp_number==0 and (player_number==3 or player_number==4):
        print compWin
    elif comp_number==1 and (player_number==0 or player_number==4):
        print compWin
    elif comp_number==2 and (player_number==0 or player_number==1):
        print compWin
    elif comp_number==3 and (player_number==1 or player_number==2):
        print compWin
    elif comp_number==4 and (player_number==2 or player_number==3):
        print compWin

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric