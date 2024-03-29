from time import time


def test(n, fn, *fn_params):
    avg = 0
    for i in range(n):
        start = time()
        fn(*fn_params)
        end = time()
        avg += end - start
    return avg


def print_test(title: str, *results):
    print(title.upper())
    for result in results:
        print(f"\t{result}")
    print("\n")
