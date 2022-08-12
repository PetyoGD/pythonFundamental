string_num = input().split()
list_corr = []
for i in string_num:
    trans_num = float(i)
    list_corr.append(abs(trans_num))
print(list_corr)
