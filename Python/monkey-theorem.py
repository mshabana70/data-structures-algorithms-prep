# Monkey Theorem Self Check
# https://runestone.academy/ns/books/published/pythonds3/Introduction/DefiningFunctions.html

# import random module
import random

# create a list of possible values for our string
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
target_string = "methinks it is like a weasel"
# Write the first function to generate a random string 28 characters long
def generate_random():
    random_string = ""
    for _ in range(len(target_string)):
        random_string += random.choice(letters)
    return random_string

generated_string = generate_random()
print(f"The generated string: {generated_string}")