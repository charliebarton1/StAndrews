
amount = 0
while amount < 50:
    y = int(input("Insert Coin: "))
    if y ==5 or y ==10 or y==25:
        print(y)
    else:
        y = 0
        print(y)
    amount += y
    print(amount)
    print(f"Amount Due: {50 -amount }")
print(f"Change Owed: {amount - 50}")


