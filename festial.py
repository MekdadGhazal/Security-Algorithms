def f(right, sub_key):
    print("The function is working...")
    temp1 = []
    for i in range(len(right)):
        if right[i] == '0':
            temp1.append(0)
        else:
            temp1.append(1)
    return temp1


def swap(a, b):
    temp1 = a
    a = b
    b = temp1
    return a , b


def xor(a, b):
    temp = []
    for i in range(len(a)):
        if a[i] == b[i]:
            temp.append(0)
        else:
            temp.append(1)

    return temp


p = input()

left = []
right = []

for i in range(int(len(p) / 2)):
    left.append(p[i])
    right.append(p[int(len(p) / 2) + i])


print(left,right)

right = f(right, 1)
left = xor(right,left)
right, left = swap(right,left)

print(f"Left = {left} ,Right = {right}")
