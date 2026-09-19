def main ():
    mass = int(input("Enter m:"))
    joules = emcsquare(mass)
    print(joules)

def emcsquare(mass):
    c = 300000000
    return mass * c ** 2

main()
