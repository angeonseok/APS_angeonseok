"""
N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

#입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

#출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(root, graph, N):
    depth = [-1] * (N+1)
    parent = [0] * (N+1)
    depth[root] = 0
    q = deque([root])

    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if depth[nxt] == -1:
                depth[nxt] = depth[node] + 1
                parent[nxt] = node
                q.append(nxt)

    return depth, parent

def lca(u, v, depth, parent):
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]

    while u != v:
        u = parent[u]
        v = parent[v]

    return u

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth, parent = bfs(1, graph, n)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    lca_node = lca(u, v, depth, parent)
    print(lca_node)