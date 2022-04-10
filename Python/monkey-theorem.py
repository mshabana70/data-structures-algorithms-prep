# Monkey Theorem Self Check
# https://runestone.academy/ns/books/published/pythonds3/Introduction/DefiningFunctions.html

# import random module
import random

# create a list of possible values for our string
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
target_string = "methinks it is like a weasel"
# Write the first function to generate a random string 28 characters long
def generate_random(strlen):
    letters = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res += letters[random.randrange(27)]
    return res

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
            random_string = generate_random(28)
            test_score = score(random_string, target_string)
            if test_score > best_score:
                best_score = test_score
                best_string = random_string
        iterations += 1
        print(f"After {iterations} iterations, {best_score} is the highest score with string: {best_string}")
    return iterations

def run_loop_two():
    best_score = 0.0
    best_string = ""
    iterations = 0
    goalString = 'methinks it is a weasel'
    testString = generate_random(len(goalString))
    while testString != goalString:
        testString = generate_random(len(goalString))
        for i in range(len(testString)):
            while testString[i] != goalString[i]:
                testString_list = list(testString)
                testString_list[i] = generate_random(1)
                testString = testString.join(testString_list)
                print(testString)
        print(testString)



# Test run loop function 
run_loop_two()


# Following the tutorial vid

# def generateOne(strlen):
#     letters = "abcdefghijklmnopqrstuvwxyz "
#     res = ""
#     for i in range(strlen):
#         res += letters[random.randrange(27)]
#     return res

# def score_2(goal, testString):
#     numSame = 0
#     for i in range(len(goal)):
#         if goal[i] == testString[i]:
#             numSame += 1
#     return float(numSame / len(goal))

# def main():
#     goalString = "methinks it is like a weasel"
#     newString = generateOne(28)
#     best_score = 0
#     best_string = ""
#     newScore = score(goalString, newString)
#     while newScore < 1:
#         if newScore >= best_score:
#             print(f"New String: {newString}")
#             best_score = newScore
#         newString = generateOne(28)
#         newScore = score(goalString, newString)
    

# main()