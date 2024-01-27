# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
import numpy


def arrays(arr):
    return numpy.array(list(map(lambda n: float(n), arr)))[::-1]
