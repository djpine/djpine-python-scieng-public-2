a, b, c = input("Input 3 comma-separated integers: ").split(",")
a, b, c = int(a), int(b), int(c)
if a > b and a > c:
    max = a
elif b > c:
    max = b
else:
    max = c
print(max)
