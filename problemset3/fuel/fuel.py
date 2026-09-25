while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y: raise ValueError;
        calculated = round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        continue 
    else:
           if calculated <= 1:
                print("E")
           elif calculated >= 99:
                print("F")
           else:  
                print(f"{calculated}%")
    break
