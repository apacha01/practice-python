# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true

import numpy


coefficients = numpy.array(input().split(), float)
x = float(input())

print(numpy.polyval(coefficients, x))
