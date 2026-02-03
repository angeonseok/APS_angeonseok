# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#입력
#첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

#출력
#첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# def counting_sort(A,B,k) : #원본, 출력, 최댓값
#     #1. 카운팅
#     cnts = [0] *(k+1)
#     for i in range(N):
#         cnts[A[i]] += 1
#     #2. 누적
#     for i in range(1, k+1):   #14568
#         cnts[i] += cnts[i-1]
#     #3. 자리배치
#     for i in range(N-1, -1, -1):
#         B[cnts[A[i]] - 1] = A[i]
#         cnts[A[i]] -= 1


# data = [0, 1, 4, 3, 1, 4, 2, 1]
# N = len(data)
# result = [0] * N
# counting_sort(data, result, max(data)+1)
# print(result)


#문제가 예의가 없네
import sys
input = sys.stdin.readline

n = int(input())

cnt = [0] * 10001

for _ in range(n):
    cnt[int(input())] += 1

for i in range(1, 10001):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i)