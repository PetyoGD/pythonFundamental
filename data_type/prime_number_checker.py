num = int(input())
flag = False
for i in range(2, num):
    if num % i == 0:
        flag = True
if flag:
    print("False")
else:
    print("True")
