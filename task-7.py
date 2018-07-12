import random

attempts = 0
num_of_6 = 0
probability = 0

analitic_solution = (1 / 3) - (1 / 36)
analitic_solution = round(analitic_solution, 3)

while probability != analitic_solution:
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    if (r1 == 6 or r2 == 6):
        num_of_6 += 1
    attempts += 1
    if num_of_6 != 0:
        probability = num_of_6 / attempts
        probability = round(probability, 3)
print("Number of attempts:", attempts)
print("Probability:", probability)

