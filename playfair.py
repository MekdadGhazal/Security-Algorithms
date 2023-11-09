# This function to sum the boolean number:
def sum1(r):
    res = 0
    for i in range(len(r)):
        res += r[i]
    return res


# letter list
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
               "w", "x", "y", "z"]

# the word
word = input("WRITE YOUR TEXT : ")

# the key
key = input("WRITE YOUR KEY : ")

# helper list [bool] to know the letters in KEY
letter_bool = []
for i in range(len(letter_list)):
    letter_bool.append(0)
# this is makes the letter_number in helper list : 1
for i in key:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            letter_bool[j] = 1

# letter in [check] used to complete the Alphapet_array  [5*5] makes it like letter_bool
letter_in = []
for i in range(len(letter_bool)):
    letter_in.append(letter_bool[i])

# this variable helps to insert the letter word in list
s = sum1(letter_in)

# this is the word without repeater letter
res = []
for i in key:
    for j in range(len(letter_list)):
        if i == letter_list[j] and letter_bool[j] == 1:
            letter_bool[j] = 0
            res.append(i)
# print(res)

# array 5*5 all elements is zeros
n = 5
m = 5
a = [0] * 5
for i in range(n):
    a[i] = [0] * m

# use it to insert the res in the array
k = 0
for i in range(5):
    for j in range(5):
        if s > 0:
            a[i][j] = res[k]
            k += 1
            s -= 1

# this variables use to know where the last insert done!
row = (int)(k / 5)
col = k % 5

# to fill array with correct letters
for i in range(len(letter_list)):
    if letter_in[i] == 1:
        continue
    else:
        a[row][col] = letter_list[i]
        col += 1
        if col == 5:
            col = 0
            row += 1
# # --------------
# # array :
# print(a)
# # --------------



# PROCESSING ORIGINAL WORD

text_after_process = []
for i in range(len(word) - 1):
    text_after_process.append(word[i])
    if word[i] == word[i + 1]:
        text_after_process.append('z')
text_after_process.append(word[len(word) - 1])
if (len(text_after_process) % 2 == 1):
    text_after_process.append('z')

# print(text_after_process)


# CRYPTO

def indexed(q):
    for j in range(5):
        for t in range(5):
            if a[j][t] == q:
                return j, t


final = []
for i in range(0, len(text_after_process), 2):
    e, b = indexed(text_after_process[i])
    c, d = indexed(text_after_process[i + 1])
    # print(e, b, c, d)
    if e == c:
        final.append(a[e][(b + 1) % 5])
        final.append(a[c][(d + 1) % 5])
    elif b == d:
        final.append(a[(e + 1) % 5][b])
        final.append(a[(c + 1) % 5][d])
    else:
        final.append(a[c][b])
        final.append(a[e][d])

print(final)
