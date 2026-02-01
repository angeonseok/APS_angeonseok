# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

#입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이다.

#출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

import sys
input=sys.stdin.readline

t = int(input().rstrip())
num = [int(input()) for _ in range(t)]
max_num = max(num)                          #입력값 중 젤 큰놈을 찾아

   
p = [True] * (max_num+1)                    #그 놈 기준으로 소수를 찾아놔
p[0] = False
p[1] = False

for i in range(2, int(max_num ** 0.5)+1):
    if p[i]:
        for j in range(i * i, max_num + 1, i):
            p[j] = False

pm = [k for k in range(2, max_num + 1) if p[k]]

for i in num:               
    cnt = 0
    for j in pm:
        if j > i // 2:      # n = p - (n - p)로 본다면 절반 날려도 되지않나
            break
        if p[i - j] :       # n - p가 소수라면 카운팅
            cnt += 1
    print(cnt)
