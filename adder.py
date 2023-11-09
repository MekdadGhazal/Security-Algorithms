letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

plain_text = input(" Enter the text : ").strip()
k = int(input(" Enter the key : "))

crypto = []

for i in plain_text:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            crypto.append((j + k) % 26)

print(crypto)

res = []
for i in crypto:
    res.append(letter_list[i].upper())
print(res)

cipher_text = input(" Enter the Cipher Text : ").strip()
k = int(input(" Enter the key : "))

decrypto = []

for i in cipher_text:
    for j in range(len(letter_list)):
        if i.lower() == letter_list[j]:
            decrypto.append((j - k) % 26)

res = []
for i in decrypto:
    res.append(letter_list[i])
print(res)
