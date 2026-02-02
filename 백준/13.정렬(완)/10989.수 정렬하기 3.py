# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#입력
#첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

#출력
#첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys
input = sys.stdin.readline


# #구글의 힘을 빌렸다...
# n = int(input())
# num = [int(input()) for i in range(n)]

# #정렬 수행할 배열 생성. 숫자의 갯수정보도 같이
# cnt = [0] * (max(num) + 1)
# for n in num :
#     cnt[n] += 1

# # 누적합으로 갱신
# for i in range(1, len(cnt)):
#     cnt[i] += cnt[i-1]

# #정렬할 리스트와 같은 길이의 리스트 생성. 이 후 작업은 니가 보면서 생각해라
# result = [0] * (len(num))
# for k in num:
#     idx = cnt[k]
#     result[idx - 1] = k
#     cnt[k] -= 1

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