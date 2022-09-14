

# Functions go here :...
def yes_no(question):

    valid = False
    while not valid:

        # asks user for input
        response = input(question).lower()
        # assesses response as yes/no or prompts correct input
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or "n":
            response = "no"
            return response
        else:
            print("Please enter yes or no")


def instructions() :
    print("****How to play****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main routine goes here...
played_before = yes_no("have you played the"
                                "game before")

if played_before == "no":
    instructions()

print("program continues")
