import sys

maximum = 0
temp = 1
str = list(sys.stdin.readline().rstrip().upper())
arr = []

for i in range(len(str)):
    str[i] = ord(str[i])

for i in range(65, 91):
    arr.append(str.count(i))

    if str.count(i) >= temp:
        temp = str.count(i)
        maximum = i

if arr.count(max(arr)) > 1:
    print('?')
else:
    print(chr(maximum))

