# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy

n, m = map(int, input().split())

M = numpy.array([input().split() for i in range(n)], int)

print(numpy.mean(M, axis=1))
print(numpy.var(M, axis=0))
print(numpy.round(numpy.std(M), 11))
