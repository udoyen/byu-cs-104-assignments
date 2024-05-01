# Pseudocode
# Print a greeting.
# Ask for a name.
# Collect the name entered by the user and store it in a variable called name.
# Ask the user what city they were born in.
# Collect the name of the city entered by the user and store it in a variable called city.
# Create a message by combining literal strings (strings you define) and the information stored in the variables (Represented below by curly braces and variable names, for example: {city} ) into a meaningful message. Think of it as a Mad Lib:
   # "Hello, " + {name} + "! I have heard that {city} is a fascinating place!" or
   # "Good morning, " + {name} + "! I have always wanted to visit {city} !"    (or something similar)
# Print out the message!

name = input("Welcome, What is your name? ") # prints a greeting and asks for a name
city = input("Hi, " + name + "! Nice meeting you! What city were you born? ") # Gets the name of the city where user was born
message = "Oh, " + name + "! I have heard of " + city + " and would love to visit it!" # Generates the message to be display to the user
print(message) # prints the message to the console
