def xor(a, b):
    res = []
    for i in range(8):
        if a[i] == b[i]:
            res.append(0)
        else:
            res.append(1)
    return res


def shift_left(num):
    temp = []
    for i in range(1, len(num)):
        temp.append(num[i])
    temp.append(0)

    return temp


def mult(num):
    temp1 = num
    temp2 = []
    if num[0] == 0:
        temp2 = shift_left(num)
    else:
        temp2 = shift_left(num)
        temp2 = xor(temp2, [0, 0, 0, 1, 1, 0, 1, 0])

    return xor(temp1, temp2)


print(mult([1, 0, 0, 1, 0, 1, 1, 0]))
