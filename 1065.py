import sys

def func(n):
    cnt = 0
    for i in range(1, n + 1):
        a = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        else:
            if (a[1] - a[0]) == (a[2] - a[1]):
                cnt += 1
    print(cnt)

n = int(sys.stdin.readline().rstrip())
func(n)
