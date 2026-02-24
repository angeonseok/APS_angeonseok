"""
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

#입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

#출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]

#벽을 부쉈는지 아닌지 체크하기 위해 3차원 배열로 생성
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

#큐에 벽을 부순 정보(status:0 안부숨, 1 부숨)도 함께 집어넣기
def bfs(start_x, start_y, status):
    q = deque()
    q.append((start_x, start_y, status))
    visited[start_x][start_y][0] = 1

    while q:
        x, y, status = q.popleft()
        for dir in ((0,1),(1,0),(0,-1),(-1,0)):
            nx,ny = x + dir[0], y + dir[1]

            #여기까지는 정상적인 bfs
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and visited[nx][ny][status] == 0:
                    visited[nx][ny][status] = visited[x][y][status] + 1
                    q.append((nx,ny,status))

                #벽을 만나고, 아직 벽을 안부쉈으면(status=0) 부수고(status=1) 진행
                elif maze[nx][ny] == 1 and visited[nx][ny][1] == 0 and status == 0:
                    visited[nx][ny][1] = visited[x][y][status] + 1
                    q.append((nx,ny,1))

bfs(0,0,0)

a = visited[n-1][m-1][0]
b = visited[n-1][m-1][1]

#도착불가능
if a == 0 and b == 0:
    print(-1)
#벽을 뚫었을 때 만 도달 가능
elif a == 0:
    print(b)
#왜뚫음?
elif b == 0:
    print(a)
#두 가지 경우 다 가능하면 최소경로
else:
    print(min(a, b))