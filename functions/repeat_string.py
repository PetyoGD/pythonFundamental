str_series = input()
num_operation = int(input())
oper =  lambda a, b: a * b
result = oper(str_series, num_operation)
print(result)

# oper= lambda str_series, num_operation: str_series * num_operation
# result = oper(input(), int(input()))
# print(result)
