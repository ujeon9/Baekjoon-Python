import sys


def solve(a):
    return sum(a)


arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(solve(arr))
