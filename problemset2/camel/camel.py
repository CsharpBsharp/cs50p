variable = input("camelCase: ")
snake_case = "".join(["_" + char if char.isupper() else char for char in variable]).lower()
print(snake_case)
