factor_num = int(input())
count_num = int(input())
multiples_list = []
trans_num = 0
for i in range(count_num):
    trans_num += factor_num
    multiples_list.append(trans_num)
print(multiples_list)
