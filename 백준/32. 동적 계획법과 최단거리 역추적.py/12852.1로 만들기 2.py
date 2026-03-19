"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

#입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

#출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.
"""

import sys
input = sys.stdin.readline

#이전 인덱스 저장용 배열까지 생성
n = int(input())
dp = [0] * (n + 1)
trace = [0] * (n + 1)

#인덱스를 저장하면서 가야하기 떄문에 min 안쓰고 ㅇㅇ
#dp배열에 값을 저장하면서 trace에 이전 인덱스까지 저장
for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    trace[i] = i - 1

    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            trace[i] = i//2

    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            trace[i] = i//3

#역추적 과정
cur = n
ans = []

while cur != 1:
    ans.append(cur)
    cur = trace[cur]

#결과가 1인데 같이 나와야지
ans.append(1)

print(dp[n])
print(*ans)