import math # import math module

condition = True # set the initial condition to True

while condition: # check the current value of the condition
    number = int(input("Enter a number ")) # Get number from a user and casts to int
    if int(math.sqrt(number)) == math.sqrt(number): # compare to see if both are the same value and return a boolean
        print(str(number) + " is a perfect square root") # print number is a perfect square
    else:
        print(str(number) + " does not have a perfect square root") # print number is not a perfect square
    answer = input("would you like to enter another number (y/n)? ") # Asks user if they wish to continue with the game
    if answer.upper() == "N": # Checks user's response
        condition = False # sets condition to False
        
print("Thank you for playing!") # Prints good bye message to user