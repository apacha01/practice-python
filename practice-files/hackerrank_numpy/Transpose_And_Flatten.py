# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy


n, m = map(int, input().split())

matrix = [input().split() for i in range(n)]

M = numpy.array(matrix, int)

print(M.transpose())
print(M.flatten())
