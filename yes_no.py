
show_instructions = ""

while show_instructions != "xxx":
    # Ask user if they have played before
    show_instructions = input("Have you played lucky unicorn before?")

    # If yes, "output continues"
    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("progress continues")

    # If no output "display instructions"
    elif show_instructions.lower() == "no" or show_instructions == "n":
        print("display instructions")

    else:
        print("please enter yes or no")



