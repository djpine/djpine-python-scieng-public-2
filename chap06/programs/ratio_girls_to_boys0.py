girls = int(input("Enter number of girls on team: "))
boys = int(input("Enter number of boys on the team: "))
try:
    print(f"Ratio of girls to boys: {girls / boys:0.2f}")
except ZeroDivisionError:
    print("There are no boys on the team so the ratio is undefined")
