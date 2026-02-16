"""
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.
i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

#입력
첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
(1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)

#출력
#과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    stone = list(map(int, input().split()))
    
    for k in range(m):
        i, j = map(int,input().split())
        cnt = 0     #조사 횟수

        #실제 인덱스는 i-1이라 조정함
        a = i - 2
        b = i
        while cnt < j:

            #주어진 경우 밖으로 나가면
            if a < 0 or b > n-1:
                break

            if stone[a] == stone[b]:
                stone[a] = 1 - stone[a]
                stone[b] = 1 - stone[b]

            a -= 1
            b += 1
            cnt +=1
        
    print(f'#{tc}', *stone)