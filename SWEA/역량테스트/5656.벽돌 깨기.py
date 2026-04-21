"""
구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.
구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.
( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )
게임의 규칙은 다음과 같다.
① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
② 벽돌은 숫자 1 ~ 9 로 표현되며,
   구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
아래는 벽돌에 적힌 숫자와, 구술이 명중했을 시 제거되는 범위의 예이다.
③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
예를 들어 아래와 같이 4 번 벽돌에 구술이 명중할 경우,
9번 벽돌은 4 번 벽돌에 반응하여,
동시에 제거된다.
④ 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.
N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.
N, W, H, 그리고 벽돌들의 정보가 주어질 때,
▶ 남은 벽돌의 개수를 구하라!

[제약 사항]
1. 1 ≤ N ≤ 4
2. 2 ≤ W ≤ 12
3. 2 ≤ H ≤ 15

[입력]
가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.
 

[출력]
출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.
(t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)
"""

from collections import deque
 
dirs = ((0,1), (1,0), (0,-1), (-1,0))
 
#1. 터트린다
def boom(a, arr):
    q = deque()
 
    for i in range(H):
        if arr[i][a] != 0:
            q.append((i, a, arr[i][a]))
            arr[i][a] = 0
            break
 
    while q:
        x, y, r = q.popleft()
 
        for k in range(1, r):
            for dir in dirs:
                nx, ny = x + dir[0] * k, y + dir[1] * k
 
                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if arr[nx][ny] != 0:
                    q.append((nx, ny, arr[nx][ny]))
                    arr[nx][ny] = 0
    return arr
 
#2. 내려간다
def fall(arr):
    for i in range(W):
        temp = []
        for j in range(H):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
                arr[j][i] = 0
 
        nj = H-1
        for v in reversed(temp):
            arr[nj][i] = v
            nj -= 1
 
    return arr
 
#3. 센다
def count(arr):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                cnt += 1
    return cnt
 
#4. 종합선물세트
def sol(depth, arr):
    global ans
    cnt = count(arr)
    ans = min(ans, cnt)
 
    if depth == N or cnt == 0:
        return
 
    for i in range(W):
        clone = [row[:] for row in arr]
        boom(i, clone)
        fall(clone)
        sol(depth+1, clone)
 
T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
 
    ans = 987654321
    sol(0,arr)
 
    print(f"#{tc} {ans}")