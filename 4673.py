def d():
    arr1 = []
    for num in range(1, 10001):
        a = []
        a.append(num)
        while (num != 0):
            a.append(num % 10)
            num = num // 10
        arr1.append(sum(a))

    arr2 = set(range(1, 10001))
    return (sorted(set(arr2) - set(arr1)))


result = d()
for i in range(len(result)):
    print(result[i])
