import sys, random
def compute(n):
    i = 0; s = 0
    while i < n: # error 3
        s += random.random()
        i += 1
    return s/n
n = int(sys.argv[1]) # error 2
print ('average of %d random numbers is %g' % (n, compute(n))) #error 1
