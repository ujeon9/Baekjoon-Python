n = int(input())
first = n
i = 0
while (True):
    i = i + 1
    a = n % 10
    b = n // 10
    tmp = a + b

    if tmp >= 10:
        tmp %= 10

    n = a * 10 + tmp
    if n == first:
        break

print(i)