num = int(input())
wagons = [0] * num
series_command = input()

while series_command != "End":
    series = series_command.split(" ")
    command = series[0]
    wagon = int(series[1])
    if command == "add":
        wagons[-1] += wagon
    elif command == "insert":
        peoples = int(series[2])
        given_wagon = wagon
        wagons[wagon] += peoples
    elif command == "leave":
        wagons[wagon] -= int(series[2])
    series_command = input()
print(wagons)
