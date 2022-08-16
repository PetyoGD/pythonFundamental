command_series = input()
removed_num = ["0"] * 10
while command_series != "End":
    command_separate = command_series.split("-")
    frase = command_separate[1]
    order_num = int(command_separate[0])
    removed_num.pop(order_num)
    removed_num.insert(order_num, frase)
    command_series = input()
removed_num = [x for x in removed_num if x != "0"]

print(removed_num)
