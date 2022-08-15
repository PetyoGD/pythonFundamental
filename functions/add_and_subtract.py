def add_and_subtract(a, b, d):
    c = a + b
    e = c - d
    return e


def sum_numbers(a, b):
    c = a + b
    return c


def subtract(c, d):
    e = c - d
    return e


first_num = int(input())
second_num = int(input())
third_num = int(input())
add = sum_numbers(first_num, second_num)
subtract = subtract(add, third_num)
print(add_and_subtract(first_num, second_num, third_num))
