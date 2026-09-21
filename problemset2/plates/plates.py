def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s=""):
    slen = len(s)
    num_detected=False
    if 2<=slen<=6 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isnumeric() and not num_detected:
                if char=="0": 
                    return False
                num_detected=True
            elif char.isalpha() and num_detected:
                return False 
        return True
    return False

main()


# 1. min len > 1 and first 2 char are letters
# 2. max len < 7
# 3. Numbers at end only not in middle
# 4 First number cannot be 0
# 5. Only letters or numbers
