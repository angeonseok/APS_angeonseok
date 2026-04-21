"""
N*N 크기의 정사각형 모양의 방에 사람들이 앉아 있다.
점심을 먹기 위해 아래 층으로 내려가야 하는데, 밥을 빨리 먹기 위해 최대한 빠른 시간 내에 내려가야 한다.
방 안의 사람들은 P로, 계단 입구를 S라고 했을 때 [Fig. 1]은 사람의 위치와 계단 입구의 위치를 표시한 모습이다.
[Fig. 1]
이동 완료 시간은 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간이다.
사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동 시간과 계단을 내려가는 시간이 포함된다.
    ① 계단 입구까지 이동 시간
        - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
        - 이동 시간(분) = | PR - SR | + | PC - SC |
          (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)
    ② 계단을 내려가는 시간
        - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
        - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
        - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
        - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
        - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.
사람의 위치와 계단 입구의 위치 및 계단의 길이 정보가 표시된 N*N 크기의 지도가 주어진다.
이때, 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우를 찾고,
그 때의 소요시간을 출력하는 프로그램을 작성하라.

[제약 사항]
1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 3초
2. 방의 한 변의 길이 N은 4 이상 10 이하의 정수이다. (4 ≤ N ≤ 10)
3. 사람의 수는 1 이상 10 이하의 정수이다. (1 ≤ 사람의 수 ≤ 10)
4. 계단의 입구는 반드시 2개이며, 서로 위치가 겹치지 않는다.
5. 계단의 길이는 2 이상 10 이하의 정수이다. (2 ≤ 계단의 길이 ≤ 10)
6. 초기에 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 서로 겹치지 않는다.

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 방의 한 변의 길이 N이 주어진다.
다음 N줄에는 N*N 크기의 지도의 정보가 주어진다.
지도에서 1은 사람을, 2 이상은 계단의 입구를 나타내며 그 값은 계단의 길이를 의미한다.

[출력]
테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.
각 줄은 "#x"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)
정답은 이동이 완료되는 최소의 시간을 출력한다.
"""

def calc(arr, length):
    if not arr:
        return 0

    # 도착 시간 빠른 순으로 처리
    arr.sort()
    end = []

    for i in range(len(arr)):
        # 처음 3명은 도착하면 바로 내려감
        if i < 3:
            start = arr[i]
        else:
            # 4번째부터는 3명 제한 때문에 앞에서 3칸 먼저 들어간 놈 끝날 때까지 대기 가능
            start = max(arr[i], end[i - 3])

        # 내려가기 시작한 시간 + 계단 길이 = 끝나는 시간
        end.append(start + length)

    # 마지막 사람 끝나는 시간이 그 계단 종료 시간
    return end[-1]


def dfs(idx):
    global ans

    # 모든 사람 계단 배정 끝났으면 시간 계산
    if idx == len(people):
        t1 = calc(stair1_people[:], stair1_len)
        t2 = calc(stair2_people[:], stair2_len)
        ans = min(ans, max(t1, t2))
        return

    x, y = people[idx]

    # 1번 계단 가는 경우
    # 계단까지 이동시간 + 계단 입구 도착 후 1분
    dist1 = abs(x - stair1[0]) + abs(y - stair1[1]) + 1
    stair1_people.append(dist1)
    dfs(idx + 1)
    stair1_people.pop()

    # 2번 계단 가는 경우
    # 계단까지 이동시간 + 계단 입구 도착 후 1분
    dist2 = abs(x - stair2[0]) + abs(y - stair2[1]) + 1
    stair2_people.append(dist2)
    dfs(idx + 1)
    stair2_people.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    # 사람 위치랑 계단 위치 따로 저장
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] >= 2:
                stairs.append((i, j))

    stair1 = stairs[0]
    stair2 = stairs[1]
    stair1_len = board[stair1[0]][stair1[1]]
    stair2_len = board[stair2[0]][stair2[1]]

    # 각 계단으로 가는 사람들 도착 시간 저장용
    stair1_people = []
    stair2_people = []
    ans = float('inf')

    # 사람마다 어느 계단 갈지 완탐
    dfs(0)

    print(f'#{tc} {ans}')