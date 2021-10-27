alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()
cnt = 0
temp = 0

for i in range(len(str)):
    for j in alphabet:
        if (len(str) > 2):
            if (str[i - 2] + str[i - 1] + str[i]) == j:
                temp += 3
                cnt += 1
                i += 2
                break
            elif (str[i - 1] + str[i]) == j:
                temp += 2
                cnt += 1
                i += 1
                break
        elif (str[i - 1] + str[i]) == j:
            temp += 2
            cnt += 1
            i += 1
            break

cnt += (len(str) - temp)
print(cnt)
