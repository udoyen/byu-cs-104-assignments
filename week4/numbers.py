import math # import math module

condition = True # initial condition to True

while condition: # check the current state of condition
    print() # prints a blank line
    number = int(input("Please enter a whole number (i.e. an integer): ")) # get number from user and cast to int
    print() # prints a blank line
    print("The number you entered is " + str(number) + ".") # print the number entered by user
    
    # check if number is even or odd
    if number % 2 == 0: # check if the number is even
        print(str(number) + " is an even number.") # print the number is even
    else:
        print(str(number) + " is an odd number.") # print the number is odd

    # check if number has a perfect square
    if int(math.sqrt(number)) == math.sqrt(number): # checks if the number has a perfect square root
        print(str(number) + " has a perfect square root.") # print the number has a perfect square root
    else:
        print(str(number) + " does not have a perfect square root.") # print the number does not have a perfect square root
        
    # Find the factors of the number
    factors = [1] # initialize a non-empty factors list
    for i in range(2, number): # loops over potential factors of number
        if number % i == 0: # check if i is a factor
            factors.append(i) # appends to the factors list
    factors.append(number) # appends the number to the factors list
    print("The factors of " + str(number) + " are " + ",".join([str(s) for s in factors]) + ".") # print the factors of number
    
    print() # prints a blank line
    print() # prints a blank line
    
    # Ask user if they wish to continue the game
    answer = input("Would you like to enter another number? (Y/n)? ") # ask user if they wish to continue the game
    if answer.upper() == "N": # checks user answer
        condition = False # sets the condition to False
print() # print a blank line     
print("Thank you for playing!") # prints a farewll message
    
    