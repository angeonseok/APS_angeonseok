"""
교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.
탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
지하 터널 어딘가에서 은신 중인 것으로 추정된다.
터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.
탈주범은 시간당 1의 거리를 움직일 수 있다.
지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.
지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.

[제약 사항]
1. 시간 제한 : 최대 50개 테이트 케이스를 모두 통과하는데, C/C++/Java 모두 1초
2. 지하 터널 지도의 세로 크기 N, 가로 크기 M은 각각 5 이상 50 이하이다. (5 ≤ N, M ≤ 50)
3. 맨홀 뚜껑의 세로 위치 R 은 0 이상 N-1이하이고 가로 위치 C 는 0 이상 M-1이하이다. (0 ≤ R ≤ N-1, 0 ≤ C ≤ M-1)
4. 탈출 후 소요된 시간 L은 1 이상 20 이하이다. (1 ≤ L ≤ 20)
5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장된다.
6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재한다.

[입력]
첫 줄에 총 테스트 케이스의 개수 T가 주어진다.
두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.
각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.
숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.

[출력]
테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.
각 줄은 “#x”로 시작하고 공백을 하나 둔 다음 정답을 기록한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)
출력해야 할 정답은 탈주범이 위치할 수 있는 장소의 개수이다.
"""

from collections import deque

dirs = ((-1,0), (0,1), (1,0), (0,-1))

pipeline = {
    1 : (0, 1, 2, 3),
    2 : (0, 2),
    3 : (1, 3),
    4 : (0, 1),
    5 : (1, 2),
    6 : (2, 3),
    7 : (0, 3)
}

#상호 연결 확인
def link(i, j, ni, nj):
    for d in pipeline[arr[ni][nj]]:
        a, b = ni + dirs[d][0], nj + dirs[d][1]
        
        if a == i and b == j:
            return True
    
    return False

#즐거운 bfs
def bfs(x, y):
    q = deque()
    cnt = 0

    q.append((x, y))
    visited[x][y] = 1
    cnt += 1

    while q:
        x, y = q.popleft()

        #l초 이후는 구할 필요가 없다
        if visited[x][y] == l:
            continue

        for d in pipeline[arr[x][y]]:
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            #서로 연결된 경우 이동 후 카운팅
            if arr[nx][ny] != 0 and visited[nx][ny] == 0:
                if link(x, y, nx, ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    ans = bfs(r, c)
    print(f"#{tc} {ans}")