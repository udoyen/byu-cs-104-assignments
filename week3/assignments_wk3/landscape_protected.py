# Authorization flow
# 1. Surround the landscape.py program with a conditional (true/false or Boolean) statement that is dependent upon a variable called authorized.
# 2. Prior to the execution of the conditional statement using authorized, a text file called credentials.txt needs to be opened and its contents read into a list.
# #### The text file can be downloaded using the link above.
# #### The structure of the data contained in the text file is known: a single line containing username, password, authorization level in comma-separated form.
# #### The text file needs to be placed in the same folder as landscape.py. Those using Replit can upload the text file into the same directory as main.py.
# 3. A pre-defined dictionary, having keys 'user', 'pass' and 'level' is to be initialized using the list created by reading the text file. The dictionary will be name credentials.
# 4. A prompt and an input is performed to collect a username.
# 5. A prompt and an input is performed to collect a password.
# 6. The collected username and password are compared with the contents of the credentials dictionary to determine whether or not they match. A token (named authorized) is set to reflect the outcome of that comparison.
# 7. As mentioned in step one, the value of authorized determines whether or not the program runs. If authorized evaluates to True, the program runs.
# 8. If authorized evaluates to False, and error message is presented to the user with the message that their credentials are invalid. 

import math # import the math module


authorized = False # Variable used to determine access
credentials = {} # Container for credentials

with open('credentials.txt', 'r') as file: # Helps to open, read, and close the file when done
    file_content = file.readline() # Read the contents of the file
    split_string_by_comma = file_content.split(',') # Split the read string by the comma
    credentials['user'] = split_string_by_comma[0] # Set the user key in the dictionary
    credentials['pass'] = split_string_by_comma[1] # Set the pass key in the dictionary
    credentials['level'] = split_string_by_comma[2][:2] # Set the level key in the dictionary and remove the '/n' character

username = input("Please enter your username! ") # Get username from user
password = input("Please enter your password! ") # Get password from user

print() # prints a blank line

if username == credentials['user'] and password == credentials['pass']: # Compares the enter credentials to the stored one
    authorized = True # Update the value of the authorized token


if authorized:

    # Set important variables
    cost_of_fertilizer_per_bag = 27 # Set the cost of a bag of fertilizer
    area_covered_by_one_bag = 2000 # Set the area covered by one bag
    area_covered_per_hour_by_tech = 2500 # Set the area covered in an hour
    charge_per_hour_of_work = 20 # Set labor cost per hour

    input("Welcome to to the Fertilizer Calculator! I will ask you for the length and width of four rectangular sections. Please enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions! Press ENTER to start!") # Give instructions to the user
    print() # prints a blank line

    L1 = float(input("What is the length of the front section?")) # Get length of rectangle 1
    w1 = float(input("What is the width of the front section?")) # Get width of rectangle 1

    L2 = float(input("What is the length of the rear section?")) # Get length of rectangle 2
    w2 = float(input("What is the width of the rear section?")) # Get the width of rectangle 2

    L3 = float(input("What is the length of the left section?")) # Get the length of rectangle 3
    w3 = float(input("What is the width of the left section?")) # Get the length of rectangle 3

    L4 = float(input("What is the length of the right section?")) # Get the length of rectangle 4
    w4 = float(input("What is the width of the right section?")) # Get the width of rectangle 4


    if L1 < 0 or w1 < 0 or L2 < 0 or w2 < 0 or L3 < 0 or w3 < 0 or L4 < 0 or w4 < 0: # Check for negative numbers

        print() # prints a blank line
        print("You entered a negative number, please restart the program!") # Inform user of a negative number use    

    else:
        
        # Calculate area of each rectangle

        area_of_rect1 = L1 * w1 # Get the area of rectangle 1
        area_of_rect2 = L2 * w2 # Get the area of rectangle 2
        area_of_rect3 = L3 * w3 # Get the area of rectangle 3
        area_of_rect4 = L4 * w4 # Get the area of rectangle 4

        # Calculate total area of all rectangles
        total_area = area_of_rect1 + area_of_rect2 + area_of_rect3 + area_of_rect4  # Get the total area of all rectangles by adding each



        bags_needed = math.ceil(total_area / area_covered_by_one_bag) # Calculate the number of bags needed and round the value

        unrounded_bags = total_area / area_covered_by_one_bag # Calculate the number of bags needed without rounding

        cost_of_fertilizer = bags_needed * cost_of_fertilizer_per_bag # Calculates total cost of fertilizer

        hours_of_labor_needed = math.ceil(total_area / area_covered_per_hour_by_tech) # Calculate time cost of work and round the value

        cost_of_labor = hours_of_labor_needed * charge_per_hour_of_work # Calculate total labor cost

        total_project_cost = cost_of_fertilizer + cost_of_labor # Calculate the total project cost

        nitro_used = unrounded_bags * 1 # Calculate the quantity of nitro fertilizer used
        potassium_used = unrounded_bags * .125 # Calcualte the quantity of potassium fertilizer used

        print() # prints a blank line
        print("Your application has a total area of %0.0f sq. feet. That will require %d bags of fertilizer. The cost of the fertilizer will be $%0.2f.\nOur technicians will require %d hours to finish the job and the labor cost will be $%0.2f. The total cost to the company will be $%0.2f. The application will result in %0.3f pounds of nitrogen and %s pounds of potassium being added to the soil" % (total_area, bags_needed, cost_of_fertilizer, hours_of_labor_needed, cost_of_labor, total_project_cost, nitro_used, str(potassium_used).lstrip("0"))) # report all quantities
else:
    print('Error: Credentials are invalid!')
