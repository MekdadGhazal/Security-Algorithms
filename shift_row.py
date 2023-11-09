def shift_row(list, round):
    temp = []
    for i in range(round, len(list)):
        temp.append(list[i])
    if len(temp) != len(list):
        k = 0
        for i in range(len(temp), len(list)):
            temp.append(list[k])
            k += 1

    return temp

print(shift_row([15,1,0,3],0))
print(shift_row([15,1,0,3],1))
print(shift_row([15,1,0,3],2))
print(shift_row([15,1,0,3],3))