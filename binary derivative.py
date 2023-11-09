def xor(a, b):
    res = 0
    if a == b:
        res = 0
    else:
        res = 1
    return res


n = int(input("Enter the length : "))

str = []
for i in range(n):
    str.append(int(input()))

f = int(input("Enter the n of F : "))

if f > n:
    print("0")
elif f < 0:
    print("Error 404")
else:
    for i in range(f):
        str_n = [0] * (n - i - 1)
        ni = 0
        for j in range(n - i - 1):
            str_n[j] = xor(str[j], str[j + 1])
            if xor(str[j], str[j + 1]) == 1 :
                ni += 1
        print(f"p = {ni/(n - i - 1)}")
        str = str_n
