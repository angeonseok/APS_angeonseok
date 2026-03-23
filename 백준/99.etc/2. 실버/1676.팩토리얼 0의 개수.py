"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

#출력
첫째 줄에 구한 0의 개수를 출력한다.
"""

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return str(result)

n = int(input())
num = fac(n)

cnt = 0
for i in reversed(num):
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)