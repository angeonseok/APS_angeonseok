"""
방향 그래프가 주어졌을 때, 그 그래프를 SCC들로 나누는 프로그램을 작성하시오.
방향 그래프의 SCC는 우선 정점의 최대 부분집합이며, 그 부분집합에 들어있는 서로 다른 임의의 두 정점 u, v에 대해서 u에서 v로 가는 경로와 v에서 u로 가는 경로가 모두 존재하는 경우를 말한다.
예를 들어 위와 같은 그림을 보자. 이 그래프에서 SCC들은 {a, b, e}, {c, d}, {f, g}, {h} 가 있다. 물론 h에서 h로 가는 간선이 없는 경우에도 {h}는 SCC를 이룬다.

#입력
첫째 줄에 두 정수 V(1 ≤ V ≤ 10,000), E(1 ≤ E ≤ 100,000)가 주어진다. 이는 그래프가 V개의 정점과 E개의 간선으로 이루어져 있다는 의미이다. 다음 E개의 줄에는 간선에 대한 정보를 나타내는 두 정수 A, B가 주어진다. 이는 A번 정점과 B번 정점이 연결되어 있다는 의미이다. 이때 방향은 A → B가 된다.
정점은 1부터 V까지 번호가 매겨져 있다.

#출력
첫째 줄에 SCC의 개수 K를 출력한다. 다음 K개의 줄에는 각 줄에 하나의 SCC에 속한 정점의 번호를 출력한다. 각 줄의 끝에는 -1을 출력하여 그 줄의 끝을 나타낸다. 각각의 SCC를 출력할 때 그 안에 속한 정점들은 오름차순으로 출력한다. 또한 여러 개의 SCC에 대해서는 그 안에 속해있는 가장 작은 정점의 정점 번호 순으로 출력한다.
"""

import sys
sys.setrecursionlimit(100000)   #재귀를 2번 돌려서 걸어야함

def kosaraju(graph, r_graph, V):
    visited = [False] * (V + 1)
    order = []


    def dfs1(v):
        visited[v] = True
        for nxt in graph[v]:
            if not visited[nxt]:
                dfs1(nxt)

        #다 보고 나오면서 순서 저장. 나중에 종료 순서 역순으로 봐야됨
        order.append(v)

    for v in range(1, V+1):
        if not visited[v]:
            dfs1(v)

    visited = [False] * (V + 1)
    sccs = []

    #역방향 그래프에서 연결된 애들 다 묶기
    def dfs2(v, scc):
        visited[v] = True
        scc.append(v)
        for nxt in r_graph[v]:
            if not visited[nxt]:
                dfs2(nxt, scc)
    
    #종료 순서의 역순으로 보면서 역방향 그래프 dfs 함 돌리기
    while order:
        v = order.pop()

        if not visited[v]:
            scc = []
            dfs2(v, scc)
            sccs.append(scc)
    
    return sccs

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
r_graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)

sccs = kosaraju(graph, r_graph, v)

#출력 조건에 맞게 정렬 및 가공
for scc in sccs:
    scc.sort()
    scc.append(-1)
sccs.sort(key=lambda x: x[0])

print(len(sccs))
for scc in sccs:
    print(*scc)