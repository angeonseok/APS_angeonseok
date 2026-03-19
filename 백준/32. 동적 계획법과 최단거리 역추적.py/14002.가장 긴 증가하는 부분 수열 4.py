"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

#출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
trace = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:

            #진짜 길이 늘어날 때만 갱신
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                trace[i] = j
            else:
                dp[i] = dp[i]

#dp[i] : i에서 끝나는 lis 길이
#맨 끝놈이 최대인 보장이 없다
idx = dp.index(max(dp))
ans = []

#최대 길이를 알고 있어서 좀 더 편하네
while len(ans) != max(dp):
    ans.append(arr[idx])
    idx = trace[idx]

print(max(dp))
print(*reversed(ans))   #ans는 역순으로 저장되어있음