# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy


shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=numpy.int32))
print(numpy.ones(shape, dtype=numpy.int32))
