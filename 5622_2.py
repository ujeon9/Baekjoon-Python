dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = input()
result = 0
for i in range(len(num)):
    for j in dial:
        if num[i] in j:
            result += (dial.index(j) + 3)

print(result)
