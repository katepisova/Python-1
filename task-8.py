import random, sys
n = int(sys.argv[1])
count = 0
probability = 0

for i in range(1, n):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    third = random.randint(1, 6)
    fourth = random.randint(1, 6)
    if ((first + second + third + fourth) < 9):
        count += 1

probability = count / n
print('Probability of win = ', '%g' % (probability))
if probability > 0.1:
    print("Playing this game is a good decision for you!")
else:
    print("You shouldn't play this game!")
