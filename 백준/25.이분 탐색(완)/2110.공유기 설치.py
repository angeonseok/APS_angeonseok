"""
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

#입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

#출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""
import sys
input = sys.stdin.readline

#배열, 설치 개수, 간격으로 해볼 예정
def wifi(arr, m, k):
    #최초 설치 개수
    cnt = 1
    
    #최초 설치 위치
    last = arr[0]

    #배열을 보면서 현재 위치와 설치 위치 차이가 간격보다 크다면
    for i in range(1, len(arr)):
        if arr[i] - last >= k:
            cnt += 1            #그 곳에 공유기를 설치하고               
            last = arr[i]       #설치 위치 업데이트
    
    #현재 간격으로 문제에서 원하는 설치 수가 나온다면 ㅇㅋ
    if cnt >= m:
        return True
    
    return False
    
n, m = map(int, input().split())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

#거리를 정렬해야함
arr.sort()

#설치 간격의 최소와 최대 설정
min_dist = 1
max_dist = arr[0] + arr[-1]

ans = 0

#이분 탐색으로 설치 간격 찾기
while min_dist <= max_dist:
    mid = (min_dist + max_dist) // 2

    if wifi(arr, m, mid):
        ans = mid
        min_dist = mid + 1
    
    else:
        max_dist = mid - 1

print(ans)