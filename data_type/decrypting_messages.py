key = int(input())
n = int(input())
for i in range(1, n + 1):
    symbol = input()
    corr_symbol = ord(symbol)
    last_symbol = corr_symbol + key
    char_symbol = chr(last_symbol)
    print(char_symbol, end="")
