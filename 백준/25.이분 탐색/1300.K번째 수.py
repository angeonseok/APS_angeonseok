"""
세준이는 크기가 N*N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i*j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N*N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.

#입력
첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.

#출력
B[k]를 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

#답은 최소 1, 최대 k 안에 있음
start = 1
end = k

ans = 0

# mid값을 k번쨰 값의 후보로 본다
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # i행( i, 2i, 3i, ... , n*i )에서 mid 이하 개수는 mid//i개
    # 근데 한 행에 최대 n개라서 min(mid//i, n)로 자름
    # 모든 행에 대해 mid 이하 원소 개수 카운팅
    for i in range(1, n+1):
        cnt += min(mid // i, n)

    # mid 이하가 k개 이상이면, k번째 값은 mid보다 작거나 같음(왼쪽으로 좁힘)
    if cnt >= k:
        ans = mid
        end = mid - 1

    #그 역의 경우
    else:
        start = mid + 1
        
print(ans)