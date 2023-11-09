def binary(a):
    res = []
    while a != 0:
        res.append(a % 2)
        a = int(a / 2)

    return res


def res(a, x, n):
    y = 1
    x = binary(x)
    for i in range(len(x)):
        if x[i] == 1:
            y = (y * a) % n
        a = pow(a, 2) % n
    return y


print(" (a ^ x) % n ")
a = int(input("Enter a : "))
x = int(input("Enter x : "))
n = int(input("Enter n : "))
res = res(a, x, n)
print(f"the result is : {res}")
