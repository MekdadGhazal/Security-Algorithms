import numpy as np

def sum1(r):
    res = 0
    for i in range(len(r)):
        res += r[i]
    return res

def swap (a ,b):
    t = a
    a = b
    b = t
    return a,b


# letter list
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

word = "ahmad"
key = "sally"
key2 = "yousha"

#
# # the word
# word = input("WRITE YOUR TEXT : ")
# # the  first key
# key = input("WRITE YOUR KEY : ")
# # The second key
# key2 = input("WRITE YOUR 2st KEY: ")


# helper list [bool] to know the letters in KEY
letter_bool = []
for i in range(len(letter_list)):
    letter_bool.append(0)

# this is makes the letter_number in helper list : 1
for i in key:
    for j in range(len(letter_list)):
        if i == letter_list[j]:
            letter_bool[j] = 1

# letter in [check] used to complete the Alphabet_array  [7*7] makes it like letter_bool
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
print(res)

adfgvx = ["A", "D", "F", "G", "V", "X"]

n = 7
m = 7
a = [0] * 7
for i in range(n):
    a[i] = [0] * m

for i in range(6):
    a[i + 1][0] = adfgvx[i]
    a[0][i + 1] = adfgvx[i]

k = 0
for i in range(1, 7):
    for j in range(1, 7):
        if s > 0:
            a[i][j] = res[k]
            k += 1
            s -= 1

# this variables use to know where the last insert done!
row = int(k / 7)  +1
col = k % 7 +1
if col == 1 :
    col += 1
# print( row , col)

# to fill array with correct letters
for i in range(len(letter_list)):
    if letter_in[i] == 1:
        continue
    else:
        a[row][col] = letter_list[i]
        col += 1
        if col == 7:
            col = 1
            row += 1

for i in range(7):
    print(a[i][:])

q = []
count = 0

while count != len(word):
    for i in range(1, 7):
        if count == len(word):
            break
        for j in range(1, 7):
            if word[count] == a[i][j]:
                q.append(a[i][0])
                q.append(a[0][j])
                count += 1
                break

sec_arr = []
for i in range(len(key2)):
    sec_arr.append([key2[i]])

print(q)
print(sec_arr)

sec_arr_col = int((len(q) / len(sec_arr)))

if len(q) % len(sec_arr) != 0:
    sec_arr_col += 1

# print(sec_arr_col , len(q) ,len(sec_arr))

j = 0
for i in range(len(q)):
    if j == len(sec_arr):
        j = 0
    sec_arr[j].append(q[i])
    j += 1

if not(len(q) == len(sec_arr) * sec_arr_col) :
    for i in range(len(q),len(sec_arr) * sec_arr_col):
        sec_arr[i % len(sec_arr)].append("A")

# print(len(sec_arr) * sec_arr_col)
print(sec_arr)

final = []

numeric = [0] *len(sec_arr)
for i in range(len(sec_arr)):
    for j in range(len(letter_list)):
        if sec_arr[i][0] == letter_list [j]:
            numeric[i] = j

print(numeric)

sort_arr = [0] * len(numeric)
for i in range(len(numeric)):
    sort_arr[i]= numeric[i]

for i in range(len(sort_arr)):
    for j in range( i+1 , len(sort_arr) ):
        if sort_arr[i] > sort_arr[j]:
            sort_arr[i] , sort_arr[j] = swap (sort_arr[i] , sort_arr[j])

print(sort_arr , numeric)

for i in sort_arr:
    index = 0
    for j in range(len(numeric)):
        if  i == numeric[j] :
            index = j
            break
    for i in range(1, sec_arr_col +1 ):
        # print(sec_arr[index][i])
        final.append(sec_arr[index][i])

print(final)


string_s = ""

for i in  final:
    string_s += i
print(string_s)
