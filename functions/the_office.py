emp_happiness = input().split()
happy_factor = int(input())
average_sum = 0
average_sum_list = []
average_sum_final = 0
happiest_counter = 0
int_happiness = [int(x) for x in emp_happiness]
for i in range(len(int_happiness)):
    average_sum = int_happiness[i] * happy_factor
    average_sum_final += average_sum
    temp_sum = average_sum
    average_sum_list.append(temp_sum)
average_sum_final = average_sum_final / len(int_happiness)
for y in average_sum_list:
    if y >= average_sum_final:
        happiest_counter += 1
if happiest_counter >= len(int_happiness) / 2:
    print(f"Score: {happiest_counter}/{len(int_happiness)}. Employees are happy!")
else:
    print(f"Score: {happiest_counter}/{len(int_happiness)}. Employees are not happy!")

# employees = input().split()
# factor = int(input())
# employeesloyees = list(map(lambda x: int(x) * factor, employees))