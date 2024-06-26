# A local landscaping company has experienced an explosion in its lawn care business. 
# The company needs your help to streamline their services, and would like you to 
# develop a program to assist their field technicians in calculating quantities relevant 
# to fertilizer applications: They need to know the number of bags of fertilizer needed, 
# the cost of material and labor, and the environmental impact of each application.

import math # import the math module


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



    bags_needed = math.ceil(total_area / area_covered_by_one_bag) # Calculate the number of bags needed

    unrounded_bags = total_area / area_covered_by_one_bag # Calculate the number of bags needed without rounding

    cost_of_fertilizer = bags_needed * cost_of_fertilizer_per_bag # Calculates total cost of fertilizer

    hours_of_labor_needed = math.ceil(total_area / area_covered_per_hour_by_tech) # Calculate time cost of work

    cost_of_labor = hours_of_labor_needed * charge_per_hour_of_work # Calculate total labor cost

    total_project_cost = cost_of_fertilizer + cost_of_labor # Calculate the total project cost

    nitro_used = unrounded_bags * 1 # Calculate the quantity of nitro fertilizer used
    potassium_used = unrounded_bags * .125 # Calcualte the quantity of potassium fertilizer used

    print() # prints a blank line
    print("Your application has a total area of %0.0f sq. feet. That will require %d bags of fertilizer. The cost of the fertilizer will be $%0.2f.\nOur technicians will require %d hours to finish the job and the labor cost will be $%0.2f. The total cost to the company will be $%0.2f. The application will result in %0.3f pounds of nitrogen and %s pounds of potassium being added to the soil" % (total_area, bags_needed, cost_of_fertilizer, hours_of_labor_needed, cost_of_labor, total_project_cost, nitro_used, str(potassium_used).lstrip("0"))) # report all quantities
