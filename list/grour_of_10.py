number_string = [int(n) for n in input().split(", ")]
group_of_10 = 10
counter = 0
while counter < len(number_string):
    collected_num = []
    for digit in number_string:
        if group_of_10 - 10 <= digit <= group_of_10:
            collected_num.append(digit)
            counter += 1
    print(f"Group of {group_of_10}'s: {collected_num}")
    group_of_10 += 10
