# Isaacs Epic Text Adventure
# Based on work by Willie Crowther & Don Woods (Colossal Cave Adventure, 1975-1977)

# Declare Variables Before Game Start
instructions = """
To play the game, type short phrases into the command line below. If you type the
word "look," the game gives you a description of your surroundings.  Typing
"inventory" tells you what you're carrying.   "Get" "drop" and "throw" helps
you interact with objects.  Part of the game is trying out different commands and
seeing what happens.  Type "help" at any time for game instructions.
"""


print("Welcome to Isaac's Epic Text Adventure!")
print("")

print("Would you like instructions?")
userInput = input("> ")
if userInput == 'yes' or userInput == 'Yes' or userInput == 'YES':
    print(instructions)
elif userInput == 'no' or userInput == 'No' or userInput == 'NO':
    print("<START GAME>")
