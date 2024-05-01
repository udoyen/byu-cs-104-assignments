# Program to half any parsed in number
# till we get to one

# Psuedocode
# Set counter to 0
# Ask for a number greater than or equal to 2
# Divide the number by 2 (into half) using the python / operator
# increase the counter value by 1
# check the result if it is 1
# Repeat the division if the result was greater than 1
# stop when result gets one


def get_number():
    counter = 0
    number = int(input('Enter a whole number greater than 1: '))
    result = number // 2
    while result != 1:
        counter += 1
        result = result // 2
    
    print('count: ' + str(counter))
    
get_number()

        