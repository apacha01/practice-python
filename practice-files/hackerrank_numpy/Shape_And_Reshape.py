# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy

inp = list(map(lambda c: int(c), input().strip().split(" ")))
arr = numpy.array(inp)
print(numpy.reshape(arr, (3, 3)))
