"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

#입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

#출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.
LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
"""

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n = len(s1)
m = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

# 두 글자가 같으면 대각위치값 +1
#아니면 위나 왼쪽 중 큰 값
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = []
cur_i, cur_j = m, n

#(m,n)에서 dp계산을 역산하면서 올라갈 예정
while cur_i > 0 and cur_j > 0:

    #글자가 서로 같으면 답에 넣고, 대각선으로 이동
    if s1[cur_j - 1] == s2[cur_i - 1]:
        ans.append(s1[cur_j - 1])
        cur_i -= 1 
        cur_j -= 1

    #아니라면 둘 중 큰 쪽으로만 이동
    elif dp[cur_i - 1][cur_j] > dp[cur_i][cur_j - 1]:
        cur_i -= 1
    else:
        cur_j -= 1   


print(dp[m][n])
print("".join(ans[::-1]))