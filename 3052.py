import sys
arr=[]

for i in range(10):
    n=int(sys.stdin.readline().rstrip())
    arr.append(str(n%42))

arr=set(arr)

print(len(arr))