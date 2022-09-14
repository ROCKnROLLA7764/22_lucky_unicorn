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
    while not valid:
        try:
            response = int(input(question))

            if response<= 0 or response > 10:
                print(error)
            else:
                valid = True
                return response
        except ValueError:
            print(error)

# *** MAIN ROUTINE ***

# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
# if user hasn't played before instructions are displayed
if played_before == "no":
    instructions()

# ask user how much they want to play with
how_much = int_check("How much do you want to play with? ")

