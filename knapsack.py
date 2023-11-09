letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

def binary(a):
    res = []
    i = 7
    while a != 0:
        res.append( a % 2)
        a = int(a / 2)
        i -= 1

    temp = []
    for i in range(len(res)-1 , -1 , -1 ):
        temp.append(res[i])
    return temp

def IQ(k , n):
    res = 0
    r1 = 26
    r2 = k
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = int (r1 / r2)
        r = r1 - q * r2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if r1 == 1 : res = t1

    if abs(res) >= n :
        res = res % n
        if res < 0:
            res = n + res
    else:
        if res < 0:
            res = n + res

    return res


def key_gen():
    a_len = int(input("Enter the length : "))
    a = [0] * a_len
    for i in range(a_len):
        a[i] = int(input(f"Enter a [ {i + 1} ] : "))

    r = int(input(" r = "))
    n = int(input(" n = "))

    bool = False
    c = input("IS there permutation : [Y - y |N - n]")
    temp = [0] * a_len
    if c == 'Y' or c == 'y':
        for i in range(a_len):
            temp[i] = int(input(f"Enter [ {i + 1} ] : "))
        bool = True

    t = []
    for i in range(a_len):
        t.append((a[i] * r) % n)

    res = t

    if bool:
        for i in range(a_len):
            res[i] = t[temp[i] - 1]

    print(res)


def crypto():
    a_len = int(input("Enter the length : "))
    a = [0] * a_len
    for i in range(a_len):
        a[i] = int(input(f"Enter a [ {i + 1} ] : "))

    p = input(" p = ")
    n = int(input(" n = "))
    k = 0
    for i in range(len(letter_list)):
        if p == letter_list[i]:
            k = i
            break
    print(k)
    k = binary(k)
    print(k)

    temp =[]
    if len(k) != a_len :
        for i in range(len(k),a_len):
            temp.append(0)
        k = temp + k

    print(k)
    res = []
    for i in range(a_len):
        res.append(a[i] *k[i])
        print(res)

    sumi = sum(res)

    return sumi


key_gen()
s = crypto()
print(s)