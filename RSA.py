def IQ(k, base):
    res = 0
    r1 = base
    r2 = k
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = int(r1 / r2)
        r = r1 - q * r2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if r1 == 1: res = t1

    if abs(res) >= base:
        res = res % base
        if res < 0:
            res = base + res
    else:
        if res < 0:
            res = base + res

    return res


def binary(a):
    res = []
    while a != 0:
        res.append(a % 2)
        a = int(a / 2)

    return res


def sam(a, x, n):
    y = 1
    x = binary(x)
    for i in range(len(x)):
        if x[i] == 1:
            y = (y * a) % n
        a = pow(a, 2) % n
    return y


m = int(input("Enter M : "))
e = int(input("Enter e : "))
q = int(input("Enter q : "))
p = int(input("Enter p : "))

n = p * q
o = (p - 1) * (q - 1)
d = IQ(e, o)
res = sam(m, e, n)

print(res)

# DECRYPTO

c = int(input("Enter C : "))
d = int(input("Enter d : "))
q = int(input("Enter q : "))
p = int(input("Enter p : "))

n = p * q
o = (p - 1) * (q - 1)
e = IQ(d, o)
res = sam(c, e, n)

print(res)
