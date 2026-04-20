"""
등산로를 조성하려고 한다.
등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.
등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.
등산로를 만드는 규칙은 다음과 같다.
   ① 등산로는 가장 높은 봉우리에서 시작해야 한다.
   ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
       즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
   ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.
이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.

[제약 사항]
1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
5. 지도에서 가장 높은 봉우리는 최대 5개이다.
6. 지형은 정수 단위로만 깎을 수 있다.
7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K가 차례로 주어진다.
그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.

[출력]
테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
출력해야 할 정답은 만들 수 있는 가장 긴 등산로의 길이이다.
"""

dirs = ((0, 1), (1, 0), (0, -1), (-1,0))

#2. 탐색하자
def dfs(i, j, length, cut):
    global ans
    ans = max(ans, length)

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:

            #3. 안깎고 가는 경우 > 그냥 진행
            if arr[ni][nj] < arr[i][j] and not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj, length + 1, cut)
                visited[ni][nj] = False

            #4. 깎을 수 있고, 깎고 가는 경우 > 깎아서 진행 후 복원(tmp로 원래 값 저장 미리해두기)
            elif not cut and arr[ni][nj] - k < arr[i][j] and not visited[ni][nj]:
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1

                visited[ni][nj] = True
                dfs(ni, nj, length + 1, True)
                visited[ni][nj] = False
                arr[ni][nj] = tmp
    

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    ans = 0

    #1. 최대 높이 봉우리 찾기
    max_h = max(max(row) for row in arr)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_h:
                visited[i][j] = True
                dfs(i, j, 1, False)
                visited[i][j] = False

    print(f"#{tc} {ans}")