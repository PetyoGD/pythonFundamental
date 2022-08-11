energy = 100
coins = 100
command_str = input().split("|")
command_num = len(command_str)
flag = False
for type_command in range(command_num):
    type_init = command_str[type_command].split("-")
    order = type_init[0]
    value = int(type_init[1])
    if order == "rest":
        if energy == 100:
            print(f"You gained {0} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += value
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")
    elif order == "order":
        if energy - 30 >= 0:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {order}.")
        else:
            print(f"Closed! Cannot afford {order}.")
            flag = True
            break
if not flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
