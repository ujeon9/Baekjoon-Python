import sys

str = sys.stdin.readline().strip()
if len(str) == 0:
    print(0)
else:
    print(str.count(' ') + 1)
