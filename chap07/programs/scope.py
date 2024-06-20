def f():
    y = "enclosing"
    z = "enclosing"
    print(f"(2) inside f: x={x}, y={y}, z={z}")

    def g():
        z = "local"
        print(f"(3) inside g: x={x}, y={y}, z={z}")

    g()
    print(f"(4) inside f: x={x}, y={y}, z={z}")


x = "global"
y = "global"
z = "global"
print(f"(1)  in main: x={x}, y={y},    z={z}")
f()
print(f"(5)  in main: x={x}, y={y},    z={z}")


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
