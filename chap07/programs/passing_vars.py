import numpy as np


def f(stg, flt, tup, dct, lis, arr):
    stg = "I am doing fine"
    flt = np.pi ** 2
    tup = (1.1, 2.9)
    dct["Dave"] = 70.1
    lis[-1] = 'end'
    arr[0] = 963.2
    return stg, flt, tup, dct, lis, arr


stg = "How do you do?"
flt = 5.0
tup = (97.5, 82.9, 66.7)
dct = {"Lucy": 3.2e6, "Ardi": 4.4e6}
lis = [3.9, 5.7, 7.5, 9.3]
arr = np.array(lis)

print('******************* Before function call ******************')
print(f"stg = {stg}")
print(f"flt = {flt:4.2f}")
print(f"tup = {tup}")
print(f"dct = {dct}")
print(f"lis = {lis}")
print(f"arr = {arr}")
print('***********************************************************')
print('********************** function call **********************')

stg1, flt1, tup1, dct1, lis1, arr1 = f(stg, flt, tup, dct, lis, arr)

print('************** Variables returned by function *************')
print(f"stg1 = {stg1}")
print(f"flt1 = {flt1:4.2f}")
print(f"tup1 = {tup1}")
print(f"dct1 = {dct1}")
print(f"lis1 = {lis1}")
print(f"arr1 = {arr1}")
print('**********  Original variables after function call ********')
print(f"stg = {stg}")
print(f"flt = {flt:4.2f}")
print(f"tup = {tup}")
print(f"dct = {dct}")
print(f"lis = {lis}")
print(f"arr = {arr}")
print('***********************************************************')


"""
Introduction to Python for Science & Engineering, 2nd Edition
by David J. Pine
"""
