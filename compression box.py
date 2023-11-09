def compression(arr):
    temp = []

    for i in range(len(arr)):
        if (i + 1) % 4 == 0: continue
        temp.append(arr[i])

    return temp


arr = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]

temp = compression(arr)
print(temp)