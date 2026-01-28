import sys

t = int(sys.stdin.readline())       #stdin.readline을 쓰면 이렇게 할 수 있다

for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)