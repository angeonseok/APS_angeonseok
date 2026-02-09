"""
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

#출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
"""
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int, input().split()))

#인덱스 조정
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = lst[i-1] + prefix[i-1]  #0 5 9 12 14 15

#계산
for _ in range(m):
    i, j = map(int,input().split())
    print(prefix[j] - prefix[i-1])