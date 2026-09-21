word=input("Input: ")
remved="".join(["" if char.lower() in ["a","e","i","o","u"] else char for char in word])
print(f"Output: {remved}")