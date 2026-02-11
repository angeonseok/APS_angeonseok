"""
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

#입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

#출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l = int(input())
    a, b = map(int,input().split())
    c, d = map(int, input().split())

    mat = [[0] * l for _ in range(l)]

    q = deque()
    mat[a][b] = 0       #이동 횟수
    q.append((a,b))     #시작지점 제공함

    while q:
        x, y = q.popleft()
        
        #종료조건
        if x == c and y ==d:
            print(mat[c][d])
            break
        
        #나이트는 8방향 이동
        for dir in [(-2,1), (-1,2), (1, 2), (2,1), (2,-1), (1,-2), (-1,-2),(-2,-1)]:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 <= nx < l and 0 <= ny < l and mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx,ny))