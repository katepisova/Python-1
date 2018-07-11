import sys, cmath
try:
    outfilename = sys.argv[1]
except:
    print("Usage:", sys.argv[0], "outfile")
    sys.exit(1)
ofile = open(outfilename, 'w')
def myfunc(y):
    if y >= 0.0:
        return y ** 5 * cmath.exp(-y)
    else:
        return 0.0
i = 2
while i < sys.argv.__len__():
    x = float(sys.argv[i])
    y = float(sys.argv[i + 1])

    fy = myfunc(y)
    ofile.write('(%g, %g)\n' % (x, fy))
    i += 2
ofile.close()
