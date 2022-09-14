import random

# main routine goes here
tokens = ["unicorn","unicorn","horse", "horse", "horse"
          "zebra", "zebra", "zebra"
          "donkey", "donkey","donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range (0,500):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
            balance += 7
    elif chosen == "donkey":
         balance -= 4
    else:
        balance -= 0.5


print()
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final balance: ${:.2f}".format(balance))
