"""
해야 할 V개의 작업이 있다. 이들 중에 어떤 작업은 특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자.
이런 작업의 선행 관계를 나타낸 그래프가 주어진다.
이 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현된다.
단, 이 그래프에서 사이클은 존재하지 않는다 (사이클은 한 정점에서 시작해서 같은 정점으로 돌아오는 경로를 말한다).
V개의 작업과 이들 간의 선행 관계가 주어질 때, 일을 끝낼 수 있는 작업 순서를 찾는 프로그램을 작성하라.
가능한 작업 순서가 여러 가지일 경우, 여러분은 이들 중 하나만 제시하면 된다.

[입력]
10개의 테스트케이스가 주어진다.
각 케이스의 첫번째 줄에는 그래프의 정점의 개수 V(3 ≤ V ≤ 1000)와 간선의 개수 E(2 ≤ E ≤ 3000)가 주어지고, 그 다음 줄에는 E개의 간선이 나열된다.
간선은 간선을 이루는 두 정점으로 표기된다.
예를 들어, 정점 5에서 28로 연결되는 간선은 “5 28”로 표기된다.
정점의 번호는 1부터 V까지의 정수값을 가지며, 입력에서 이웃한 수는 모두 공백으로 구분된다.
 
[출력]
각 케이스마다 '#x'(x는 테스트케이스의 번호이며 1부터 시작한다)를 출력하고 올바른 작업 순서를 공백으로 구분하여 출력한다.
"""

#전형적인 위상정렬
from collections import deque

T = 10
for tc in range(1, T+1):
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)

    #그래프 연결 + 차수 부여
    for i in range(0,len(arr),2):
        a = arr[i]
        b = arr[i+1]
        graph[a].append(b)
        indegree[b] += 1
    
    #차수 0인 친구들 부터 꺼내기
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        node = q.popleft()
        ans.append(node)

        #차수를 점차 감소시키면서 0이 되면 다음 순서로 나올 준비
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(f"#{tc} " + " ".join(map(str, ans)))