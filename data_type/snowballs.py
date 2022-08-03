snowballs = int(input())
best_value = 0
last_quality = 0
last_time = 0
last_weight = 0
for num in range(1, snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = int((snowball_weight / snowball_time)) ** snowball_quality
    if best_value < value:
        best_value = value
        last_quality = snowball_quality
        last_time = snowball_time
        last_weight = snowball_weight
print(f"{last_weight} : {last_time} = {best_value} ({last_quality})")
