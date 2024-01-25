from common import print_test, test


def create_new_list_from_integer_list_with_comprehension(list):
    return [n * n for n in list]


def create_new_list_from_integer_list_with_map(list):
    return map(lambda n: n * n, list)


print("List comprehension vs Map\n")
print_test(
    "1000 Iterations",
    f'{"AVG with comprehension:":50} {test(1000,create_new_list_from_integer_list_with_comprehension,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
    f'{"AVG with map:":50} {test(1000,create_new_list_from_integer_list_with_map,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
)
print_test(
    "10000 Iterations",
    f'{"AVG with comprehension:":50} {test(10000,create_new_list_from_integer_list_with_comprehension,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
    f'{"AVG with map:":50} {test(10000,create_new_list_from_integer_list_with_map,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
)
print_test(
    "100000 Iterations",
    f'{"AVG with comprehension:":50} {test(100000,create_new_list_from_integer_list_with_comprehension,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
    f'{"AVG with map:":50} {test(100000,create_new_list_from_integer_list_with_map,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),)}',
)

"""
List comprehension vs Map

1000 ITERATIONS
        AVG with comprehension:                            0.0009584426879882812
        AVG with map:                                      0.0005178451538085938


10000 ITERATIONS
        AVG with comprehension:                            0.010931253433227539
        AVG with map:                                      0.004997730255126953


100000 ITERATIONS
        AVG with comprehension:                            0.08634090423583984
        AVG with map:                                      0.027223587036132812
"""
