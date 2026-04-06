"""
강호네 회사에는 직원이 N명이 있고, 해야할 일이 M개가 있다. 직원은 1번부터 N번까지 번호가 매겨져 있고, 일은 1번부터 M번까지 번호가 매겨져 있다.
각 직원은 자신이 할 수 있는 일들 중 한 개의 일만 담당할 수 있고, 각각의 일을 담당하는 사람은 1명이어야 한다.
각각의 직원이 할 수 있는 일의 목록이 주어졌을 때, M개의 일 중에서 최대 몇 개를 할 수 있는지 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 직원의 수 N과 일의 개수 M이 주어진다. (1 ≤ N, M ≤ 1,000)
둘째 줄부터 N개의 줄의 i번째 줄에는 i번 직원이 할 수 있는 일의 개수와 할 수 있는 일의 번호가 주어진다.

#출력
첫째 줄에 강호네 회사에서 할 수 있는 일의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

def bipartite_matching(graph, left_size, right_size):
    match_left = [-1] * (left_size + 1)     #왼쪽 정점이 현재 누구랑 매칭됐는지
    match_right = [-1] * (right_size + 1)   #오른쪽 정점이 현재 누구랑 매칭됐는지

    def dfs(v, visited):
        #왼쪽 v가 연결할 수 있는 오른쪽 정점 확인
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True

            #1. 비어있거나
            #2. 이미 누가 차지중이어도, 그 놈을 다른 데 옮길 수 있으면 매칭
            if match_right[u] == -1 or dfs(match_right[u], visited):
                match_left[v] = u
                match_right[u] = v
                return True
        
        return False
    
    result = 0
    
    #왼쪽 정점 하나씩 보면서 매칭 시도
    for v in range(1, left_size + 1):
        visited = [False] * (right_size + 1)
        if dfs(v, visited):
            result += 1
    
    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    work = arr[1: cnt + 1]
    graph[i].extend(work)

ans = bipartite_matching(graph, n, m)
print(ans)