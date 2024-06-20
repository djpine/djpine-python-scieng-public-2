a = 3
for i in range(10):
    x = a ** i
    if x > 1000000:
        break
    print(x, end=' ')
print('finished')
