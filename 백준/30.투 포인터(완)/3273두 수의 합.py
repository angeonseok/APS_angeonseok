"""
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

#출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.
"""
#변수명을 바꿨으면 좀 바꾸자
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))   #정렬하고 시작
k = int(input())

#양 끝 포인터 설정
cnt = 0
l = 0
r = n -1

#양 끝에서 중앙으로
while r > l:
    s = lst[r] + lst[l]
    if s == k:
        cnt += 1
        r -= 1
        l += 1

    #크게 더한 쪽을 줄여야지
    elif s > k:
        r -= 1
    
    #작게 더한 쪽을 늘려야지
    else:
        l += 1

print(cnt)