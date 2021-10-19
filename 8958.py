import sys

n = int(sys.stdin.readline().rstrip())

string = []
sum = []

for i in range(n):
    string.append(sys.stdin.readline().rstrip())

for i in range(n):
    sum.append(0)
    cnt = 0
    for j in range(len(string[i])):
        if string[i][j] == 'O':
            cnt += 1
        else:
            cnt = 0
        sum[i] += cnt
    print(sum[i])
