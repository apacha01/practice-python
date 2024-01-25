from common import test


def repeat_strings_with_plus(string, n_repeat):
    s = ""
    for _ in range(n_repeat):
        s += string
    return s


def repeat_strings_with_mult(string, n_repeat):
    return string * n_repeat


print(test(1000, repeat_strings_with_plus, "hello", 2))
print(test(1000, repeat_strings_with_mult, "hello", 2))
