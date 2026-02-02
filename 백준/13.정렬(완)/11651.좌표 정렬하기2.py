# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

#입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

#출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())

num_list = []
for _ in range(n):
    [a, b] = map(int,input().split())
    num_list.append([a, b])

#key=lambda를 이용해 정렬조건 변경 가능. 1항 오름차순 > 0항 오름차순
num_list.sort(key= lambda x : (x[1],x[0]))

for i in num_list:
    print(i[0], i[1])