# str_num = input().split()
# oposite_num = []
# for index in range(len(str_num)):
#     single_num = -int(str_num[index])
#     oposite_num.append(single_num)
# print(oposite_num)


str_num = input().split()
oposite_num = [-int(s) for s in str_num]
print(oposite_num)
