# 정수 n(0 ≤ n ≤ 4*10e9)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

#입력
#첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

#출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

import sys

def is_prime(m):                        #소수 판별 함수
    if m == 0 or m == 1:                
        return False
    
    for i in range(2,int(m ** 0.5)+1):  # root n까지만 하는 모습
        if m % i == 0:
            return False
        
    return True


t = int(sys.stdin.readline().rstrip())
p = []

for i in range(t):
    num = int(sys.stdin.readline().rstrip())


    while 1:                    #입력받은 num값을 소수가 될 때 까지 반복 상승

        if is_prime(num):
            p.append(num)       #소수되면 모아
            break
        else :
            num +=1

for i in p:                     #답 모아서 출력
    print(i)