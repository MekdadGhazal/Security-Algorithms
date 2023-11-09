letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

plain_text = input("Enter the text : ").strip()
k = input("Enter the key : ")

text_as_num = []
key_as_num = []

for i in plain_text:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            text_as_num.append(j)

i = 0
while len(k) < len(text_as_num) :
    k += letter_list[text_as_num[i]]
    i += 1

# print(k)
for i in k:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            key_as_num.append(j)

crypto = []

for i in range(len(text_as_num)):
    crypto.append(letter_list[(text_as_num[i] + key_as_num[i]) % 26].upper())

print(crypto)


cipher_text = input("Enter the text : ").strip()
k = input("Enter the key : ")

text_as_num = []
key_as_num = []

for i in cipher_text:
    for j in range(len(letter_list)):
        if i.lower() == letter_list[j]:
            text_as_num.append(j)

# i = 0
# while len(k) < len(text_as_num) :
#     k += letter_list[text_as_num[i]]
#     i += 1
# print(k)

for i in k:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            key_as_num.append(j)

decrypto = []

for i in range(len(text_as_num)):

    decrypto.append(letter_list[(text_as_num[i] - key_as_num[i]) % 26])
    if len(key_as_num) < len(text_as_num):
        key_as_num.append((text_as_num[i] - key_as_num[i]) % 26)

print(decrypto)
