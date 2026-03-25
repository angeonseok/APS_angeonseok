"""
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

#출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
"""

import sys
input = sys.stdin.readline

INF = 10**18

#모든 경로의 가능여부 + 행렬형태 자료 > 플로이드 씀
def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue

            ik = dist[i][k]
            for j in range(n):
                nd = ik + dist[k][j]

                if nd < dist[i][j]:
                    dist[i][j] = nd


n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

#연결 안됨 > INF로 표현 변경
for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            dist[i][j] = INF

floyd(n, dist)

#도달 가능한 경우는 1, 아니면 0
for i in range(n):
    for j in range(n):
        if dist[i][j] != INF:
            dist[i][j] = 1
        else:
            dist[i][j] = 0

for row in dist:
    print(*row)