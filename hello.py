# What we have learned in day 1
print("Hello, World!")


# String concatination way not very good but ok
name = input("What is your name? ")
print("Hello, " + name)


# String with comma format concatination
print("Hello, ", name)


# Well turns out (,) format adds an extra space so lets try fixing it.
print("Hello,", name)


# Well there is a new way avaialble from 3.6 and perfected in 3.12
# wihch is using formattted string literral used with f or F and {}
print(f"Hello I am formatted string and my name is {name}")
print(F"Well here I am tried again with big F and still my name is {name}")


# Now lets try int variable types which we can cast with int() built in function
x = input("Enter first number to add: ")
y = input("Enter second number to add: ")
print(x+y)
# Well that didn't go as planned lets try it with int() casting
x = int(input("Enter first number to add again: "))
y = int(input("Enter second number to add again: "))
print(x+y)


# Howe about floats then?
x = float(input("Enter first flaot to add: "))
y = float(input("Enter second float to add:"))
print(x+y)


# How about rounding it ?
print(round(x+y))

# Now lets try some string functions
first, last = input("Enter your first and last name: ").split()
print(f"My first name is {first} and my last name is {last}.")

# Well thats fine and dandy but that doesn't solve the problem
# of some one entering name in full lower case.
first, last = input("Enter your first and last name: ").title().split()
print(f"My first name is {first} and my last name is {last}.")

# How about we just need one name and want to capitilize it ? 
# We will try two string func
first = input("Enter your first name: ").capitalize()
print(f"My first name is {first}")
first = input("Enter your first name:").title()
print(f"My first name is {first}")

