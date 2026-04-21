"""
스마트폰을 무선 충전 할 때 최적의 BC (Battery Charger)를 선택하는 알고리즘을 개발하고자 한다. [그림 1]과 같이 가로 세로 10*10 영역의 지도가 주어졌을 때, 설치된 BC 정보는 다음과 같다.
BC의 충전 범위가 C일 때, BC와 거리가 C 이하이면 BC에 접속할 수 있다. 이때, 두 지점 A(XA, YA), B(XB, YB) 사이의 거리는 다음과 같이 구할 수 있다.
D = |XA - XB| + |YA - YB|
위의 [그림 1]에서 (4,3)과 (5,4) 지점은 BC 1과 BC 3의 충전 범위에 모두 속하기 때문에, 이 위치에서는 두 BC 중 하나를 선택하여 접속할 수 있다.
매초마다 특정 BC의 충전 범위에 안에 들어오면 해당 BC에 접속이 가능하다. 따라서 T=5에 사용자 A는 BC 3에, 사용자 B는 BC 2에 접속할 수 있다. 이때, 접속한 BC의 성능(P)만큼 배터리를 충전 할 수 있다. 만약 한 BC에 두 명의 사용자가 접속한 경우, 접속한 사용자의 수만큼 충전 양을 균등하게 분배한다.
BC의 정보와 사용자의 이동 궤적이 주어졌을 때, 모든 사용자가 충전한 양의 합의 최댓값을 구하는 프로그램을 작성하라.

[제약사항]
1. 지도의 가로, 세로 크기는 10이다.
2. 사용자는 총 2명이며, 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발한다.
3. 총 이동 시간 M은 20이상 100이하의 정수이다. (20 ≤ M ≤ 100)
4. BC의 개수 A는 1이상 8이하의 정수이다. (1 ≤ A ≤ 8)
5. BC의 충전 범위 C는 1이상 4이하의 정수이다. (1 ≤ C ≤ 4)
6. BC의 성능 P는 10이상 500이하의 짝수이다. (10 ≤ P ≤ 500)
7. 사용자의 초기 위치(0초)부터 충전을 할 수 있다.
8. 같은 위치에 2개 이상의 BC가 설치된 경우는 없다. 그러나 사용자A, B가 동시에 같은 위치로 이동할 수는 있다. 사용자가 지도 밖으로 이동하는 경우는 없다.

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 총 이동 시간(M), BC의 개수(A)가 주어진다.
그 다음 2개의 줄에는 각각 사용자 A와 B의 이동 정보가 주어진다.
한 사용자의 이동 정보는 M개의 숫자로 구성되며, 각각의 숫자는 다음과 같이 매초마다 이동 방향을 의미한다.
숫자
0 : 이동안함
1 : 상
2 : 우
3 : 하
4 : 좌
그 다음 줄에는 A개의 줄에 걸쳐 BC의 정보가 주어진다.
하나의 BC 정보는 좌표(X, Y), 충전 범위(C), 처리량(P)로 구성된다.

[출력]
출력은 "#t"를 찍고 한 칸 띄운 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
정답은 모든 사용자의 충전량 합의 최대값을 출력한다.
"""

# 0 이동없음, 1 상, 2 우, 3 하, 4 좌
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    moveA = [0] + list(map(int, input().split()))
    moveB = [0] + list(map(int, input().split()))

    bc = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        bc.append((y, x, c, p))   # 행, 열로 바꿔 저장

    ax, ay = 1, 1
    bx, by = 10, 10
    ans = 0

    for t in range(M + 1):
        # 현재 시간 이동 적용
        ax += dx[moveA[t]]
        ay += dy[moveA[t]]
        bx += dx[moveB[t]]
        by += dy[moveB[t]]

        a_list = []
        b_list = []

        # 현재 위치에서 잡히는 BC 찾기
        for i in range(A):
            x, y, c, p = bc[i]

            if abs(ax - x) + abs(ay - y) <= c:
                a_list.append(i)

            if abs(bx - x) + abs(by - y) <= c:
                b_list.append(i)

        # 아무 BC도 못 쓰는 경우 대비
        a_list.append(-1)
        b_list.append(-1)

        best = 0

        # A, B가 고를 수 있는 BC 조합 전부 비교
        for ai in a_list:
            for bi in b_list:
                total = 0

                if ai == -1 and bi == -1:
                    total = 0
                elif ai == -1:
                    total = bc[bi][3]
                elif bi == -1:
                    total = bc[ai][3]
                elif ai == bi:
                    # 같은 BC 고르면 성능은 한 번만 반영
                    total = bc[ai][3]
                else:
                    total = bc[ai][3] + bc[bi][3]

                best = max(best, total)

        ans += best

    print(f'#{tc} {ans}')