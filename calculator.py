def main():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    calculate(x, y)

def calculate(x=0, y=0):
    # sum  
    # Notice how it acutally used 1 format specifiers here comma, and .2f options together
    # That format specifier contains multiple formatting options:
        # - , → use thousands separators
        # - .2 → precision of 2 digits after the decimal
        # - f → fixed-point floating-point format
    add = x + y
    print(f"sum is {add:,.2f}")

    # subtract
    sub = x - y
    print(f"Subtraction is {sub:,.2f}")

    # multiply
    mul = x * y 
    print(f"Multiplication is {mul:,.2f}")

    # division
    if y == 0:
        print("Undefined")
    else:
        div = x/y
        print(f"Division is {div:,.2f} ")

    # power 
    # method 1 simple multiplicaion 
    power1 = x * x
    power2 = y * y 
    print(f"Power of x is {power1} and Power of y is {power2} using method 1")

    # method 2 using **
    power1 = x ** 2
    power2 = y ** 2 
    print(f"Power of x is {power1} and Power of y is {power2} using method 2")

    # method 3 using pow function 
    power1 = pow(x, 2)
    power2 = pow(y, 2)
    print(f"Power of x is {power1} and Power of y is {power2} using method 3")
    
main() 

