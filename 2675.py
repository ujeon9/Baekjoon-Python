import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    temp = ""
    cnt, str = sys.stdin.readline().rstrip().split()
    for j in range(len(str)):
        print(str[j] * int(cnt), end="")
    print()
