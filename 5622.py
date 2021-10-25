str = input()
arr = []
for i in range(0, len(str)):
    for j in range(65, 91):
        if ord(str[i]) < 68:
            arr.append(2)
            break
        elif ord(str[i]) < 71:
            arr.append(3)
            break
        elif ord(str[i]) < 74:
            arr.append(4)
            break
        elif ord(str[i]) < 77:
            arr.append(5)
            break
        elif ord(str[i]) < 80:
            arr.append(6)
            break
        elif ord(str[i]) < 84:
            arr.append(7)
            break
        elif ord(str[i]) < 87:
            arr.append(8)
            break
        elif ord(str[i]) < 91:
            arr.append(9)
            break
time = 0
for i in range(len(arr)):
    time += (arr[i] + 1)

print(time)
