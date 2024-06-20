legs = int(input("Enter the total number of legs: "))
animals = int(input("Enter the total number of animals: "))

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
