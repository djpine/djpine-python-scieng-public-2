x = int(input("Input an integer divisible by 3 but not by 9: "))
if x % 3 == 0 and x % 9 != 0:
    print(x, "is divisible by 3 but not by 9")
else:
    print("Not ok")
