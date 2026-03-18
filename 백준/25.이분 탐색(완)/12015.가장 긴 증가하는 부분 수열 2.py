"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

#출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#정답을 담을 리스트
ans = []
for x in arr:

    # x가 ans에서 어디 들어가나 보자
    temp = bisect_left(ans, x)

    #ans 끝에 들어가야 되면 길이 늘어나는거라 추가
    if temp >= len(ans):
        ans.append(x)

    #아니면 기존값 갱신
    else:
        ans[temp] = x

print(len(ans))
