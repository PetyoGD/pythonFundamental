is_even = lambda x: x % 2 == 0

series_num = input().split()
series_int = [int(s) for s in series_num]
even_list = []
result = list(filter(is_even, series_int))
print(result)
