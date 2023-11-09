def cal_k(k):
    res = 0
    r1 = 26
    r2 = k
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = int (r1 / r2)
        r = r1 - q * r2
        t = t1 - q * t2
        #print(q, r1, r2, r, t1, t2, t)
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if r1 == 1 : res = t1

    if abs(res) >= 26 :
        res = res % 26
        if res < 0:
            res = 26 + res
    else:
        if res < 0:
            res = 26 + res

    return res

#
# a = cal_k(11)
# print(a)
# #
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

plain_text = input("Enter the text : ").strip()
k = int(input("Enter the key : "))

crypto = []

for i in plain_text:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            crypto.append((j * k) % 26)

print(crypto)

res = []
for i in crypto:
    res.append(letter_list[i].upper())
print(res)

cipher_text = input("Enter the Cipher Text : ").strip()
k = int(input("Enter the key : "))

k = cal_k(k)
# print(k)
decrypto = []

for i in cipher_text:
    for j in range(len(letter_list)):
        if i.lower() == letter_list[j]:
            decrypto.append((j * k) % 26)

res = []
for i in decrypto:
    res.append(letter_list[i])
print(res)
