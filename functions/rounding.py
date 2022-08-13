series = input().split(" ")
series_digit = [float(s) for s in series]
list_ = []
for i in series_digit:
    list_.append(round(i))
print(list_)
