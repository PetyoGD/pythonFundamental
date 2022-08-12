function = input()
first_num = int(input())
second_num = int(input())


def result_operation():
    if function == "multiply":
        return first_num * second_num
    elif function == "divide":
        return first_num / second_num
    elif function == "add":
        return first_num + second_num
    elif function == "subtract":
        return first_num - second_num


print(round(result_operation()))
