num_lines = int(input())
sum_lines = 0
for i in range(num_lines):
    line = int(input())
    sum_lines += line
    if sum_lines > 255:
        print("Insufficient capacity!")
        sum_lines -= line
print(f"{sum_lines}")
