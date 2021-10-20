import sys

n = int(sys.stdin.readline().rstrip())
rat = []
for i in range(n):
    cnt = 0
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    num = arr[0]
    arr.pop(0)
    avg = sum(arr) / num

    for j in range(len(arr)):
        if arr[j] > avg:
            cnt += 1

    ratio = (cnt / len(arr)) * 100
    rat.append(str(format(ratio, ".3f")) + "%")

for i in range(n):
    print(rat[i])
