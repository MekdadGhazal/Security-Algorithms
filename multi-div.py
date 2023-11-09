r1 = 26
r2 = 7

t1 = 0
t2 = 1
r = 1
while r != 0:
    q = int(r1 / r2)
    r = r1 % r2
    t = t1 - (q * t2)
    r1 = r2
    r2 = r
    t1 = t2
    t2 = t

if t1 < 0:
    print(26 + t1)
else:
    print(t1)
my_letter = []
crypto_list = []
decrypto_list = []
my_text = []
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]


def text_pro(input):
    for z in input:
        for k in range(len(letter_list)):
            if z == letter_list[k]:
                my_letter.append(k)


def crypto():
    for k in my_letter:
        crypto_list.append((k * 7) % 26)


def decrypto():
    for k in crypto_list:
        decrypto_list.append((k * t1) % 26)
    for i in decrypto_list:
        my_text.append(letter_list[i])


text_pro(input("Inter your text : ").strip())
crypto()
decrypto()
print(f"Your text after processing : {my_letter}")
print(f"Your text after crypto : {crypto_list}")
print(f"Your text after decrypto : {decrypto_list}")
print(f'Your text {"".join(my_text)}')



