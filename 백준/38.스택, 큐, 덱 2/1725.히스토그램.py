"""
히스토그램에 대해서 알고 있는가? 히스토그램은 아래와 같은 막대그래프를 말한다.
각 칸의 간격은 일정하고, 높이는 어떤 정수로 주어진다. 위 그림의 경우 높이가 각각 2 1 4 5 1 3 3이다.
이러한 히스토그램의 내부에 가장 넓이가 큰 직사각형을 그리려고 한다. 아래 그림의 빗금 친 부분이 그 예이다. 이 직사각형의 밑변은 항상 히스토그램의 아랫변에 평행하게 그려져야 한다.
주어진 히스토그램에 대해, 가장 큰 직사각형의 넓이를 구하는 프로그램을 작성하시오.

#입력
첫 행에는 N (1 ≤ N ≤ 100,000) 이 주어진다. N은 히스토그램의 가로 칸의 수이다. 다음 N 행에 걸쳐 각 칸의 높이가 왼쪽에서부터 차례대로 주어진다. 각 칸의 높이는 1,000,000,000보다 작거나 같은 자연수 또는 0이다.

#출력
첫째 줄에 가장 큰 직사각형의 넓이를 출력한다. 이 값은 20억을 넘지 않는다.
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0


for i in range(n):
    #현재 막대의 시작지점임
    start = i

    #현재 막대보다 더 큰 놈들은 넓이 계산하고 끝내
    while stack and stack[-1][1] > arr[i]:
        a, value = stack.pop()

        # 지금 높이는 더 낮은 놈
        # 방금 뽑은 막대 시작점까지 먹고 들어갈 수 있음
        start = a
        ans = max(ans, value * (i - start))

    #시작지점이랑 높이 같이 넣기
    stack.append((start, arr[i]))

#계산 안된 위치들 전부 계산하기
#맨 오른쪽에서 막대까지 거리를 밑변으로 잡으면 됨
while stack:
    start, value = stack.pop()
    ans = max(ans, value * (n - start))

print(ans)