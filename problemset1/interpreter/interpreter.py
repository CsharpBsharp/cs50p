def main():
    expression = input("Expression: ").split()
    print(f"{calculate(expression):.1f}")

def calculate(expression):
   x = float(expression[0])
   z = float(expression[2])
   match expression[1]:
        case "+":
            return x + z
        case "-":
            return x - z 
        case "*":
            return x * z
        case "/":
            return x / z 
        case _:
            return None

main()