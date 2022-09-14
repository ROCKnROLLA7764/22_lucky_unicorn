greeting = "Honey we need Money"
sides = "$" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "$" * len (greeting)
# Functions go here


print(top_bottom)
print(greeting)
print(top_bottom)
import random

# function goes here
# yes no function assesses input for yes/no answer
def yes_no(question):
    valid = False
    while not valid:
        # asks user for input
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter yes or no ")


# function to display instructions
def instructions():
    print("*** How to play ***\n")
    print("""Welcome to lucky unicorn, the cost is $1 per round to 
    play.
    If you get a unicorn you win $5.
    If you receive a Horse or a zebra you win 50c.
    A Donkey you get nothing.
    Good luck!\n""")
    return ""

# assesses number is valid and within range
def int_check(question):
    error = "please enter a whole number between 1 and 10"
    valid = False


# *** MAIN ROUTINE ***

# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
# if user hasn't played before instructions are displayed
if played_before == "no":
    instructions()

# ask user how much they want to play with
how_much = int_check("How much do you want to play with? ")
# main routine goes here
tokens = ["unicorn", "horse", "horse", "horse"
          "zebra", "zebra", "zebra"
          "donkey", "donkey","donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range (0,500):
    chosen = random.choice(tokens)
# assesses number is valid and within range


    # Adjust balance
    if chosen == "unicorn":
            balance += 4
    elif chosen == "donkey":
         balance -= 1
    else:
        balance -= 0.5


print()
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final balance: ${:.2f}".format(balance))
# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance", balance)
