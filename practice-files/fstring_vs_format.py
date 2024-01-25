from common import test


def fstring_formatting(param, param1, param2):
    return f"This is param: {param}. This is param1: {param1}. This is param2: {param2}"


def format_string_formatting(param, param1, param2):
    return "This is param: {param}. This is param1: {param1}. This is param2: {param2}".format(
        param=param, param1=param1, param2=param2
    )


print(
    f'{"AVG with f strings in 1000 iterations:":50} {test(1000, fstring_formatting, "hi", 789328, 2.3578952)}'
)
print(
    f'{"AVG with format() method in 1000 iterations:":50} {test(1000, format_string_formatting, "hi", 789328, 2.3578952)}'
)


print(
    f'{"AVG with f strings in 10000 iterations:":50} {test(10000, fstring_formatting, "hi", 789328, 2.3578952)}'
)
print(
    f'{"AVG with format() method in 10000 iterations:":50} {test(10000, format_string_formatting, "hi", 789328, 2.3578952)}'
)


print(
    f'{"AVG with f strings in 100000 iterations:":50} {test(100000, fstring_formatting, "hi", 789328, 2.3578952)}'
)
print(
    f'{"AVG with format() method in 100000 iterations:":50} {test(100000, format_string_formatting, "hi", 789328, 2.3578952)}'
)

"""
AVG with f strings in 1000 iterations:             0.0019865036010742188
AVG with format() method in 1000 iterations:       0.002431154251098633
AVG with f strings in 10000 iterations:            0.017630815505981445
AVG with format() method in 10000 iterations:      0.024208784103393555
AVG with f strings in 100000 iterations:           0.08413052558898926
AVG with format() method in 100000 iterations:     0.10445785522460938
"""
