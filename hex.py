def binary(a):
    res = [0] * 4
    i = 3
    while a != 0:
        res[i] = a % 2
        a = int(a / 2)
        i -= 1

    return res


def hexi(num):
    temp1 = int(num / 10)
    temp2 = num % 10
    temp1 = binary(temp1)
    temp2 = binary(temp2)
    temp = temp1 + temp2
    return temp


print(hexi(45))