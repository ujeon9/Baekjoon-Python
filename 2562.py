import sys

arr=[]
for i in range(9):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)

max=max(arr)

print(max, arr.index(max)+1)