condition = True # set initial value of condition to True
while condition: # check the current value of condition
    factors = [1]  # initialize a non-empty list
    number = int(input("Enter a number: ")) # get the number from user
    for i in range(2, number): # iterate over the range 2 to number
        if number % i == 0: # check the remainder of the modulus operation
            factors.append(i) # append i to the factors list
    factors.append(number) # append number to factors list
    for j in factors: # loop over the factors list
        print(j, end=' ') # print the factors list items on a straight line
    answer = input("\nWould you like to enter another number (y/n)? ") # Ask user if they want to enter another number
    if answer.upper() == "N": # check user's response
        condition = False # set the condition to False

print("Thank you for playing!") # print the farewell message
