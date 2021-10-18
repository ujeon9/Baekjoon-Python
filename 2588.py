a = int(input())
b = int(input())

result = 0
k = 1
arr = []
tmp = []

while (b != 0):
    tmp.append(b % 10)
    b = b // 10

for i in range(0, 3):
    print(tmp[i] * a)

    result += tmp[i] * a * k
    arr.append(result)
    k *= 10

print(result)
