"""
이진 트리에서 임의의 두 정점의 가장 가까운 공통 조상을 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하라.

[입력]
가장 첫 번째 줄에 테스트케이스의 수가 주어진다.
각 케이스의 첫 번째 줄에는 정점의 개수 V(10 ≤ V ≤ 10000)와 간선의 개수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어진다.
각 케이스의 두 번째 줄에는 E개 간선이 나열된다. 간선은 항상 “부모 자식” 순서로 표기된다.
위에서 예로 든 트리에서 정점 5와 8을 잇는 간선은 “5 8”로 표기된다.
정점의 번호는 1부터 V까지의 정수이며, 루트 정점은 항상 1번이다.

[출력]
각 테스트케이스마다 '#t'(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 가장 가까운 공통 조상의 번호와 그것을 루트로 하는 서브 트리의 크기를 공백으로 구분하여 출력하라.
"""

from collections import deque

T = int(input())
for tc in range(1, T+1):
    v, e, node1, node2 = map(int, input().split())
    tmp = list(map(int, input().split()))

    #재가공
    graph = [[] for _ in range(v + 1)]
    parent = [-1] * (v + 1)
    for i in range(0, len(tmp), 2):
        a = tmp[i]
        b = tmp[i + 1]
        graph[a].append(b)
        parent[b] = a

    #첫번쩨 노드의 부모들 전부 체크
    visited = [False] * (v + 1)
    now = node1
    while now != -1:
        visited[now] = True
        now = parent[now]
    
    #두번째 노드의 부모 찾아가면서 처음으로 방문처리 된 친구가 공통조상
    ans = node2
    while ans != -1:
        if visited[ans]:
            break
        ans = parent[ans]
    
    #공통조상에서부터 bfs
    cnt = 1
    q = deque([ans])
    while q:
        node = q.popleft()

        for nxt in graph[node]:
            cnt += 1
            q.append(nxt)

    print(f"#{tc} {ans} {cnt}")