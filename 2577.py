import sys

num = 1

for i in range(3):
    temp = sys.stdin.readline().rstrip()
    num = num * int(temp)

result=str(num)

for i in range(10):
    print(result.count(str(i)))


# result = list(map(int, str(num)))

# for i in range(10):
#     cnt = 0
#     for j in range(0, len(result)):
#         if i == result[j]:
#             cnt = cnt + 1
#     print(cnt)
#
