"""
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

#입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

#출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

#합한 후 나머지를 기준으로 모을 예정
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = (prefix[i-1] + arr[i-1]) % m

#나머지 수집
res = [0] * m
for j in range(1, n+1):
    res[prefix[j]] += 1

#나머지 자체가 0인 놈들만큼 일단 카운팅
ans += res[0]

#누적합을 기준으로 부분 구간의 합을 생각한다면 2개를 뽑아서 서로 빼는 형태
#즉 같은 나머지를 가진 애들 중 
for k in range(m):
    ans += res[k] * (res[k]-1) // 2

print(ans)