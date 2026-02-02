# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

#입력
#첫째 줄에 정렬하려고 하는 수 N이 주어진다. 
# N은 1,000,000,000보다 작거나 같은 자연수이다.

#출력
#첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

import sys
input = sys.stdin.readline

n = str(input().rstrip())       #입력이 2143 이런식으로 붙어서 들어옴
a = []

for i in n:                     #설명할 게 있나?
    a.append(i)

a.sort(reverse=True)

print("".join(a))
