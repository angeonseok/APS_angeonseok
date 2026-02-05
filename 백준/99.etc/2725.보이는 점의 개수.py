def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

import sys
input = sys.stdin.readline
c = int(input())

for _ in range(c):
    n = int(input().rstrip())
    cnt = 0

    for i in range(n+1):
        for j in range(n+1):
            if gcd(i,j) == 1:
                cnt += 1

    print(cnt)