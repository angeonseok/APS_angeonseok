"""
평소에 등산을 좋아하는 삼성이는 먼 산을 보면서 봉우리의 개수가 몇 개인지 궁금해졌다. N개의 지형의 높이가 주어지고, 봉우리는 높아지다가 낮아지는 지형을 봉우리로 간주한다. 단, 맨 앞쪽지형은 다음 지형이 보다 높으면 봉우리이고, 맨 뒤쪽 지형은 이전 지형보다 높으면 봉우리로 간주한다.
예) 5 3 3 5 4가 주어지면 봉우리는 2개가 된다.
N개의 지형이 주어질 때 봉우리의 수를 출력하시오.

#입력
- 첫 줄에 테스트케이스 수가 주어진다.
- 다음으로 지형의 수 N(0<=N<=100)이 주어진다
- 다음으로 지형의 높이가 N개 주어진다. (0<= 높이 <= 10)

#출력
- ‘#’ 과 테스트 케이스 번호를 출력하고 봉우리의 수를 출력한다.
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    m = list(map(int, input().split()))

    if n == 0:
        print(f'#{tc} 0')
        continue

    # 3 5 5 3 같은 경우 봉우리 1개임. 그래서 높이에 변동이 있는 경우만 다시 모아둠
    a = [m[0]]
    for x in m[1:]:
        if x != a[-1]:
            a.append(x)

    k = len(a)

    #재정리 기준으로 봉우리 조건 따지기
    ans = 0
    if k == 1:
        ans = 1
    
    elif k == 2:
        if a[0] != a[1]:
            ans = 1

    else:
        if a[0] > a[1]:
            ans += 1
        
        if a[k-1] > a[k-2]:
            ans += 1

        for i in range(1, k-1):
            if a[i] > a[i-1] and a[i] > a[i+1]:
                ans += 1

    print(f'#{tc} {ans}')