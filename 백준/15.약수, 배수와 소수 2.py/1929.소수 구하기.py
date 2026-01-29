# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

#출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys

m,n = map(int,sys.stdin.readline().split())

def is_prime(n):                        #에라토스테네스의 체
    p = [True] * (n + 1)                #1978, 11653에서도 도움 받았다.
    p[0] = False
    p[1] = False

    for i in range(2, int(n**0.5)+1):
        if p[i] :
            for j in range(i * i, n + 1, i):
                p[j] = False
    pm = [i for i in range(2, n + 1) if p[i]]

    return pm

a = is_prime(n)

for i in a :
    if i >= m:
        print(i)