h, m = map(int, input().split())

if m >= 45:
    m -= 45
elif h == 0 and m < 45:
    m += 15
    h = 23
else:
    m += 15
    h -= 1
print(h, m)
