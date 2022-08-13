def product_cal(product, num):
    if product == "coffee":
        return num * 1.50
    elif product == "water":
        return num * 1.00
    elif product == "coke":
        return num * 1.40
    elif product == "snacks":
        return num * 2.00


result = product_cal(input(), int(input()))
print(f"{result:.2f}")
