'''
Monkey Theorem using Hill Climbing (Genetic) Algorithm
reference: https://www.gkbrk.com/wiki/hill_climbing/

How does the Hill Climbing Algorithm work
(Can be broken down into four simple steps)

1. Start with an empty or random solution. This is called our best solution 
2. Make a copy of the solution and mutate it slightly
3. Evaluate the new solution. If it's better than the best solution, we replace the best solution with this one.
4. Go to step two and repeat

This can be done in three functions

1. Create a random solution
2. Evaluate a solution and return a score
3. Mutate a solution in a random way
'''

# Imports
import random
import string

# Generate Random Solution
def generate_random_solution(length=29):
    """Returns a random solution. Will be useful in population-based genetic solution in the future."""
    return [random.choice(string.printable) for _ in range(length)]


# Evaluating a solution
def evaluate(solution):
    """Return a distance metric between two strings. This function returns the absolute difference of our solution to the target."""
    target = "methinks it is like a weasel"
    diff = 0
    for i in range(len(target)):
        s = solution[i] # letter in passed in solution
        t = target[i] # letter in target solution
        diff += abs(ord(s) - ord(t)) # ord() returns the unicode of the char passed
        # print(ord(s), ord(t), diff) # the lower the difference, the more accurate it is
    return diff

# print(evaluate("metisnohc9ag ksndosjdmsoekdu"))
# print(evaluate("methinks it is like a weasel"))

# Mutating a solution
# In genetic algorithms, mutating a solution means randomely changing it in a minute way.
def mutate_solution(solution):
    """Change one of the letters randomely."""
    index = random.randrange(len(solution) - 1)
    solution[index] = random.choice(string.printable)
    # string.printable = 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 

# General outline of Hill Climbing Algorithm

best_solution = generate_random_solution(solution)
best_score = evaluate(best_solution)

while True:
    print("Best score so far", best_score, "Solution", "".join(best_solution))
    if best_score == 0:
        break
    
    new_solution = list(best_solution)
    mutate_solution(new_solution)
    score = evaluate(new_solution)
    if evaluate(new_solution) < best_score:
        best_solution = new_solution
        best_score = score


