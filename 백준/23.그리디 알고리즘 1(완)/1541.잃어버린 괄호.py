"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

#입력
첫째 줄에 식이 주어진다. 식은 '0'~'9', '+', 그리고 '-'만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

#출력
첫째 줄에 정답을 출력한다.
"""

import sys
input = sys.stdin.readline

s = input().strip()

#주어진 문자열을 "-" 기준으로 쪼개기
cut = s.split("-")

#쪼개진 문자열을 정수형으로 변환 후 합을 구하는 함수
def part_sum(string):
    sum = 0
    part = list(map(int, string.split("+")))
    for num in part:
        sum += num
    return sum

#"-"가 나오기 전까지의 합
ans = part_sum(cut[0])

#"-" 이후 다음 "-" 이전까지의  수를 합해서 빼면 됨
for i in range(1, len(cut)):
    a = part_sum(cut[i])
    ans -= a

print(ans)