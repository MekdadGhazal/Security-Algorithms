def swap(a, b):
    t = a
    a = b
    b = t
    return a, b


def binary(a):
    res = [0] * 8
    i = 7
    while a != 0:
        res[i] = a % 2
        a = int(a / 2)
        i -= 1

    return res


def decimal(a):
    res = 0
    j = 0
    for i in range(len(a) - 1, -1, -1):
        res += a[i] * pow(2, j)
        j += 1

    return res


def xor(a, b):
    res = []
    a = binary(a)
    b = binary(b)
    for i in range(8):
        if a[i] == b[i]:
            res.append(0)
        else:
            res.append(1)
    return res


letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

plain_text = [0] * 10
key = [0] * 10

# print(plain_text)

length_of_word = input("Enter the word length : ")
for i in range(int(length_of_word)):
    plain_text[i] = input(f"Enter the {i + 1} letter : ")

length_of_key = input("Enter the key length : ")
for i in range(int(length_of_key)):
    key[i] = input(f"Enter the {i + 1} letter : ")

temp = input("Each byte contain __ bit : ")
num_of_bit = pow(2, int(temp))

s = []
for i in range(0, num_of_bit):
    s.append(i)

t = []
for i in range(0, num_of_bit):
    t.append(key[i % int(length_of_key)])

j = 0
for i in range(num_of_bit):
    j = (j + int(s[i]) + int(t[i])) % num_of_bit
    s[i], s[j] = swap(s[i], s[j])

k = []
i = 0
j = 0
for count in range(int(length_of_key)):
    i = (i + 1) % num_of_bit
    j = (j + int(s[i])) % num_of_bit
    s[i], s[j] = swap(s[i], s[j])
    t = (s[i] + s[j]) % num_of_bit
    k.append(s[t])

cipher = []

for i in range(int(length_of_word)):
    cipher.append(decimal(xor(int(plain_text[i]), int(k[i]))))

print(cipher)
