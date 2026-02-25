"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

#입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

#출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())

    #맨날하는 그래프 생성
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    visited = [-1] * (v + 1)

    #이분 그래프 조건 체크용
    flag = True

    for i in range(1, v+1):
        #방문 안한 놈이 있다면
        if visited[i] == -1:
            
            #그놈을 기준으로
            q.append(i)
            
            #순회를 해
            while q:
                a = q.popleft()
                if visited[a] == -1:

                    #색칠하기
                    visited[a] = 0

                for j in graph[a]:

                    #인접 노드와 서로 다른 색으로 칠하기
                    if visited[j] == -1:
                        visited[j] = 1 - visited[a]
                        q.append(j)

                    #이미 방문한 인접 노드와 같으면 이분 그래프 아님 >> 바로 종료
                    elif visited[j] == visited[a]:
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")  