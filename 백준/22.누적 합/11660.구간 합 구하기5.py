"""
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.
1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.
표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

#입력
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

#출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
"""

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

#인덱스 맞추기
prefix = [[0] * (n + 1) for _ in range(n + 1)]

#누적합 배열 생성. 2차원은 이거다.
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

#특정 구간의 합 계산하기
for n in range(m):
    line = (list(map(int,input().split())))
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    
    #ㅇㅇ
    ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] +prefix[x1-1][y1-1]
    
    print(ans) 