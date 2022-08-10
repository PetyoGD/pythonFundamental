charity = input().split(",")
num_beggars = int(input())
final_list = []
charity_digit = [int(n) for n in charity]
counter_index = 0
in_order = len(charity_digit)
while counter_index < num_beggars:
    beggar_profit = 0
    for beggar_sum in range(counter_index, len(charity_digit), num_beggars):
        beggar_profit += charity_digit[beggar_sum]
    final_list.append(beggar_profit)
    counter_index += 1
print(final_list)
