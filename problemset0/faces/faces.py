def main ():
    capture = input("How are you feeling today : ")
    print(convert(capture))

def convert(capture):
    return capture.replace(":)", "😊").replace(":(", "🙁")
    
main()
