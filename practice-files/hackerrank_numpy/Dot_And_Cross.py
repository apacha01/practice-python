# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
import numpy


n = int(input())

A = numpy.array([input().split() for i in range(n)], int)
B = numpy.array([input().split() for i in range(n)], int)

print(A.dot(B))
