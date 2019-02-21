# Isaacs Epic Text Adventure
# Based on work by Willie Crowther & Don Woods (Colossal Cave Adventure, 1975-1977)

# Declare Variables Before Game Start
instructions = """
To play the game, type short phrases into the command line below. If you type the
word
"""


print("Welcome to Isaac's Epic Text Adventure!")
print("")

print("Would you like instructions?")
userInput = input("> ")
if userInput == 'yes' or userInput == 'Yes' or userInput == 'YES':
    print(instructions)
elif userInput == 'no' or userInput == 'No' or userInput == 'NO':
    print("<START GAME>")
