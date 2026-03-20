"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

#입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

#출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

#k+1로 하니까 걍 뛰쳐나감
q = deque()
visited = [-1] * 100001
trace = [-1] * 100001

q.append(n)
visited[n] = 0

while q:
    now = q.popleft()
    
    if now == k:
        break

    for nxt in (now - 1, now + 1, now * 2):
        if not (0 <= nxt < 100001):
            continue
        
        #이전 노드 위치만 기록해두면 끝
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            trace[nxt] = now
            q.append(nxt)   

#역추적
cur = k
ans = []
while cur != -1:
    ans.append(cur)
    cur = trace[cur]

print(visited[k])
print(*reversed(ans))