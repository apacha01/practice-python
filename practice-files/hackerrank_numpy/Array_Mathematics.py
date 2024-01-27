# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
import numpy


n, m = map(int, input().split())

N = numpy.array([input().split() for i in range(n)], int)
M = numpy.array([input().split() for i in range(n)], int)

print(N + M)
print(N - M)
print(N * M)
print(numpy.floor_divide(N, M))
print(N % M)
print(N**M)
