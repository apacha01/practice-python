# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy


n = int(input())
A = numpy.array([input().split() for i in range(n)], float)

print(numpy.round(numpy.linalg.det(A), 2))
