# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
import numpy


n, m = map(int, input().split())

A = numpy.array([input().split() for i in range(n)], int)

print(numpy.prod(numpy.sum(A, axis=0)))
