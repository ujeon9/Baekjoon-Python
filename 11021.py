import sys

n=int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    print("Case #"+str(i)+":",a+b) # 콤마(,)>공백(기본값)이 자동으로 추가, 더하기(+)>문자열을 공백없이 연결할 수 있음

