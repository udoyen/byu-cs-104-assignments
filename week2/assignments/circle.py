# Psudocode
# Ask for the radius of the circle
# Cast the radius to a float
# Calculate the diameter of the circle
# Calculate the circumference of the circle
# Calculate the area of the circle
# Output the diameter, circumference, and area of the circle using concatenation

pi = 3.14 # Create the pi variable and assign it a value of 3.14
r = float(input("What is the radius of the circle? ")) # Get the radius of the circle from the user
d = 2 * r # Calculate the diameter of the circle
c = 2 * pi * r # Calculate the circularference of the circle
A = pi * r * r # Calculate the area of the circle
result = "A circle with a radius of " + str(r) + " units will have a diameter of " + str(d) + " units, a circumference of " + str(c) + " units and an area of " + str(A) + " square units." # Creates a variable called message and set the value to the concatenated string
print(result) # pirint result of the calculation

