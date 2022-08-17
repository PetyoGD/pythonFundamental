current_version = input().split(".")
next_version = [int(x) for x in current_version]
next_version[-1] += 1
for current in range(len(next_version) - 1, -1, -1):
    if next_version[current] > 9:
        next_version[current] = 0
        if current - 1 >= 0:
            next_version[current - 1] += 1
print(".".join(str(s) for s in next_version))

# current_version = input().split(".")
# next_version = [int(x) for x in current_version]
# next_version[-1] += 1
# if next_version[2] == 10:
#     next_version[2] = 0
#     next_version[1] += 1
# if next_version[1] == 10:
#     next_version[1] = 0
#     next_version[0] += 1
# print(f"{next_version[0]}.{next_version[1]}.{next_version[2]}")
