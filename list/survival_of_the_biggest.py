import sys

list_str = input().split()
num_remove = int(input())
list_int = [int(s) for s in list_str]
small_num = sys.maxsize
num_str_input = len(list_str)
for index in range(num_remove):
    for i in range(num_str_input):
        comp_digit = list_int[i]
        if comp_digit < small_num:
            small_num = comp_digit
    list_int.remove(small_num)
    small_num = sys.maxsize
    num_str_input -= 1
    if num_str_input == num_str_input - num_remove:
        break
list_str = [str(s) for s in list_int]
print(*list_str, sep=", ")
