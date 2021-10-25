import sys

a, b = map(str, sys.stdin.readline().rstrip().split())
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)
