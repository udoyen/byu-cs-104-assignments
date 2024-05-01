import pprint  # Import this inbuild in lib to outputs in a nice manner

data = [
        {
        "type": "general",
        "setup": "What do you call a cow with no legs?",
        "punchline": "Ground beef.",
        "id": 198
        },
        {
        "type": "general",
        "setup": "What do you call a nervous javelin thrower?",
        "punchline": "Shakespeare.",
        "id": 214
        },
        {
        "type": "general",
        "setup": "What do you call a fake noodle?",
        "punchline": "An impasta.",
        "id": 206
        },
        {
        "type": "general",
        "setup": "What did the Zen Buddist say to the hotdog vendor?",
        "punchline": "Make me one with everything.",
        "id": 188
        },
        {
        "type": "programming",
        "setup": "Where did the API go to eat?",
        "punchline": "To the RESTaurant.",
        "id": 398
        },
        {
        "type": "general",
        "setup": "How many hipsters does it take to change a lightbulb?",
        "punchline": "Oh, it's a really obscure number. You've probably never heard of it.",
        "id": 140
        },
        {
        "type": "general",
        "setup": "What do you call a droid that takes the long way around?",
        "punchline": "R2 detour.",
        "id": 204
        },
        {
        "type": "general",
        "setup": "What do you call a dad that has fallen through the ice?",
        "punchline": "A Popsicle.",
        "id": 201
        },
        {
        "type": "general",
        "setup": "How does a French skeleton say hello?",
        "punchline": "Bone-jour.",
        "id": 134
        },
        {
        "type": "general",
        "setup": "How good are you at Power Point?",
        "punchline": "I Excel at it.",
        "id": 129
        }
]   # the data blob is the data you copied that was returned from the website: the JSON object

# print(data[2]['type'])   # In this line, what is the purpose of the number 2? What is the purpose of the word 'type' ?

# ---------- Sample data manipulation -------------------- #

# Create a table from the returned data

# Format the data into a list of lists
items = []


keys = list(data[0].keys()) # Get the dictionary keys from the data


items.append(keys) # Add the headers

d = [[v for v in i.values()] for i in data] # Generate the list of values using a list comprehension

for i in d: # Generate the data source
    items.append(i)
    

pprint.pprint(items)  # Print out the data source
print() # Print out a blank line
print() # Print out a blank line



column_widths = [max(len(str(row[i])) for row in items) for i in range(len(items[0]))]  # Calculate column widths based on the length of the longest string in each column using a list comprehension


print(" | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(items[0])))  # Print table headers using Python f-strings to format


print("-" * (sum(column_widths) + len(items[0]) * 3 - 1)) # Print separator

# Print table rows
for row in items[1:]: # Skip the first item in items which is the header row
    print(" | ".join(f"{str(row[i]):<{column_widths[i]}}" for i in range(len(items[0])))) # Print the values using the column widths and f-string formatting.



