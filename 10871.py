import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(arr)):
    if (x > arr[i]):
        print(arr[i], end=" ")
