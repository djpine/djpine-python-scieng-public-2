a, b, c = input("Input 3 comma-separated integers: ").split(",")
a, b, c = int(a), int(b), int(c)
max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)
