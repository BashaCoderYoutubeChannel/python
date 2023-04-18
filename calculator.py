digit1 = input("Digit 1: ")
sign = input("sign: ")
digit2 = input("Digit 2: ")
#checker
def error():
    print("Error. There was an error in the process")
try:
    if sign == "*":
        #times
        print(int(digit1) * int(digit2))
    elif sign == "+":
        #add
        print(int(digit1) + int(digit2))
    elif sign =="-":
        #subtract
        print(int(digit1) -int(digit2))
    elif sign =="/":
        #divide
        print(int(digit1) / int(digit2))
    else:
        error()
except:
    error()
