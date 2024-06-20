while True:
    try:
        legs = int(input("Enter the total number of legs: "))
        assert legs % 2 == 0
        break
    except AssertionError:
        print("Total number of legs must be an even number")
while True:
    try:
        animals = int(input("Enter the total number of animals: "))
        assert 4 * animals >= legs and 2 * animals <= legs
        break
    except AssertionError:
        print("Number of animals must be >= {} and <= {}"
              .format((legs + 2) // 4, legs // 2))

pigs = legs // 4  # maximum possible number of pigs
chickens = animals - pigs

while legs != 4 * pigs + 2 * chickens:
    pigs -= 1
    chickens += 1
    if pigs < 0:
        raise ValueError("There is no solution for these inputs.")

print("\nNumber of chickens =", chickens)
print("Number of pigs =", pigs)
print("Number of legs =", 4 * pigs + 2 * chickens)
print("Number of animals =", pigs + chickens)
