target_series = [int(t) for t in input().split()]

action_command = input().split()
temp_list = []
while action_command != ["End"]:
    target_aim = int(action_command[1])
    if action_command[0] == "Shoot":

        if 0 <= target_aim <= len(target_series):
            result = target_series[target_aim] - int(action_command[2])
            if result <= 0:
                target_series.pop(target_aim)
                action_command = input().split()
                continue
            target_series.pop(target_aim)
            target_series.insert(target_aim, result)
    elif action_command[0] == "Add":
        if 0 <= target_aim <= len(target_series):
            target_series.insert(target_aim, int(action_command[2]))
        else:
            print("Invalid placement!")
    elif action_command[0] == "Strike":
        if 0 <= target_aim <= len(target_series):
            target_series.pop(target_aim)
            if 0 <= (target_aim + int(action_command[2]) and (
                    target_aim - int(action_command[2]))) <= len(target_series):

                target_series.pop(target_aim + int(action_command[2]) - 1)
                target_series.pop(target_aim - int(action_command[2]))
            else:
                target_series.insert(target_aim, int(action_command[2]))
                print("Strike missed!")
                action_command = input().split()
                continue
    action_command = input().split()
print("|".join(str(s) for s in target_series))
