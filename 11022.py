import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #" + str(i) + ":", str(a), "+", str(b), "=", a + b)
