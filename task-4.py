from sys import *
from cmath import *
import numpy

# for n in argv[1:]:
#     if float(n) > 0:
#         print ("ln(%g)" % float(n), "=", log(float(n)))
#     else:
#         print("ln(%g)" % float(n), "is incorrect")

# for i in range(1, len(argv)):
#     if float(argv[i]) > 0:
#         print("ln(%g)" % float(argv[i]), "=", log(float(argv[i])))
#     else:
#         print("ln(%g)" % float(argv[i]), "is incorrect")

i = 1;
while i < len(argv):
    if float(argv[i])>0:
        print("ln(%g)" % float(argv[i]), "=", log(float(argv[i])))
    else:
        print("ln(%g)" % float(argv[i]), "is incorrect")
    i =  i + 1;


