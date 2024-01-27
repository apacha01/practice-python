# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
import numpy


n, m, p = map(int, input().split())

NP = numpy.array([input().split() for i in range(n)], int)
MP = numpy.array([input().split() for i in range(m)], int)

R = numpy.concatenate((NP, MP))

print(R)
