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

# Compare generated string to the target string and return a score
def score(random_string, test_string):
    score = 0
    for index in range(len(random_string)):
        if random_string[index] == test_string[index]:
            score += 1
    return float(score / len(random_string)) * 100

# Loop through generated strings and the score of such strings
def run_loop():
    best_score = 0.0
    best_string = ""
    iterations = 0
    while best_score != 100.0:
        for _ in range(1000000):
            random_string = generate_random()
            test_score = score(random_string, target_string)
            if test_score > best_score:
                best_score = test_score
                best_string = random_string
        iterations += 1
        print(f"After {iterations} iterations, {best_score} is the highest score with string: {best_string}")
    return iterations


# Test run loop function 
run_loop()