"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

#출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.
"""

#정답의 결과 != 실제 역추적 결과

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#이분 탐색 lis는 금방인데
#그 값이 있던 인덱스도 저장해야 역추적하지
#근데 그냥 저장만 한 배열만 있으면 역추적에서 막히던데
#그래서 값 저장 + 인덱스 저장 이후 이전 인덱스 저장을 따로 처리했네

ans = []            #길이별 최소 끝값
trace = []          #그 끝값이 들어있는 실제 인덱스
prev = [-1] * n     #현재 인덱스 오기 직전 인덱스

for i, x in enumerate(arr):
    temp = bisect_left(ans,x)
    
    if len(ans) <= temp:
        ans.append(x)
        trace.append(i)
    else:
        ans[temp] = x
        trace[temp] = i
    
    if temp > 0:
        prev[i] = trace[temp - 1]

result = []
cur = trace[-1]
while cur != -1:
    result.append(arr[cur])
    cur = prev[cur]

print(len(ans))
print(*reversed(result))