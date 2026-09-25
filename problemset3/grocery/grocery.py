# Version 2
quantity = {}
while True:
    try:
        item = input().upper()
        quantity[item] = quantity.get(item, 0) + 1  
    except EOFError:
        print()
        for item in sorted(quantity):
            print(quantity[item], item)
        break


# Version 1
"""
grocery = []
quantity = {}
while True:
    try:
        grocery.append(input().upper())
    except ValueError:
        continue
    except EOFError:
        grocery.sort()
        print()
        for item in grocery:
            quantity[item] = quantity.get(item, 0) + 1
        for items in quantity:
            print(quantity[items], items )
        break
"""
