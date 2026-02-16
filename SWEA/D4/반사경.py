"""
SSAFY벤처회사에서 거울을 이용한 게임을 제작하려고 한다. 거울은 2가지 방향만을 가지며, 양면 거울이다.
(0, 0)에서 오른쪽으로 레이저 빔이 출발할 때, 정사각형 격자 판 밖으로 나갈 때까지 몇 개의 거울에 레이저가 반사되는지 그 개수를 출력하는 프로그램을 작성하시오.
위 예제의 정답은 7이다.

#제약사항
1. 정사각형 격자 모양의 판에 대응되는 2차원 N X N 배열의 N은 5 이상 100 이하이다.(5 ≤ N ≤ 100)
2. (0, 0)에는 거울이 없다.

#입력
첫 줄에는 테스트 케이스의 총 수가 주어진다.
그 다음 줄부터, 테스트 케이스가 주어지는데, 각 테스트 케이스는 N+1 줄로 구성된다.
각 테스트 케이스의 첫째 줄에는 N이 주어지고, 다음 N줄에는 N X N 배열이 주어진다. N X N 배열에서 0은 아무것도 없는 공간을 나타내며, 1은 위의 예제의 [방향1] 거울, 2는 [방향 2] 거울을 나타낸다.

#출력
출력의 각 줄은 '#x'로 시작해야 하고, 공백을 하나 둔 다음 레이저가 도달하는 거울 수를 출력한다.
단, x는 테스트 케이스 번호이다.
"""

T =int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    #단방향할거임
    dx, dy = 0, 1
    x, y = 0, 0

    cnt = 0
    visited = set()

    #출발지로 오면 종료
    while True:
        state = (x, y, dx, dy)
        if state in visited:
            break
        visited.add(state)

        nx, ny = x + dx, y + dy

        #밖으로 나가면 종료
        if not (0 <= nx < n and 0 <= ny < n):
            break
            
        x, y = nx, ny
        
        #이동하고 만난 칸에 따라 방향전환
        if arr[x][y] == 1:
            dx, dy = -dy, -dx
            cnt += 1
        
        elif arr[x][y] == 2:
            dx, dy = dy, dx
            cnt += 1
    
    print(f'#{tc} {cnt}')