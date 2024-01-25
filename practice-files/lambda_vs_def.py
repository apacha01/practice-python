from common import test, print_test


# just looked for computational expensive fn since doing n + n1 didn't seem a real test


def naive_ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1))


naive_ackermann_lambda = (lambda f: lambda m, n: f(f, m, n))(
    lambda self, m, n: n + 1
    if m == 0
    else self(self, m - 1, 1)
    if n == 0
    else self(self, m - 1, self(self, m, n - 1))
)


print(f'{"AVG with def in 1000 iterations:":50} {test(1000, naive_ackermann, 3, 5)}')
print(
    f'{"AVG with lambda in 1000 iterations:":50} {test(1000, naive_ackermann_lambda, 3, 5)}'
)


print(f'{"AVG with def in 10000 iterations:":50} {test(10000, naive_ackermann, 3, 5)}')
print(
    f'{"AVG with lambda in 10000 iterations:":50} {test(10000, naive_ackermann_lambda, 3, 5)}'
)


print(
    f'{"AVG with def in 100000 iterations:":50} {test(100000, naive_ackermann, 3, 5)}'
)
print(
    f'{"AVG with lambda in 100000 iterations:":50} {test(100000, naive_ackermann_lambda, 3, 5)}'
)

"""
AVG with def in 1000 iterations:                   4.974416732788086
AVG with lambda in 1000 iterations:                5.678961992263794
AVG with def in 10000 iterations:                  50.770618200302124
AVG with lambda in 10000 iterations:               54.41389584541321
AVG with def in 100000 iterations:                 529.5331938266754
AVG with lambda in 100000 iterations:              638.182374715805
"""
