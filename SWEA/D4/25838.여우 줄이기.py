"""
길이 N 의 알파벳 소문자로 이루어진 문자열이 주어진다.
당신은 이 문자열에서 “fox” 라는 부분 문자열을 지우는 것을 반복할 수 있다.
예를 들어, “aafoxbb” 라는 문자열에서 fox를 지우면 “aabb” 가 된다.
한편, “fzozx” 는 “fox” 가 연속해 있지 않기 때문에 “zz” 로 바꿀 수 없다.
당신은 부분 문자열을 적절히 지워서 문자열의 길이를 최소화하려고 한다. 그 때의 길이는 얼마인가? 

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
각 테스트 케이스는 다음과 같이 구성되었다. 
    -  첫 번째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 200000)

    -  두 번째 줄에 길이 N 의 알파벳 소문자로 이루어진 문자열이 주어진다.

[출력]
각 테스트 케이스 마다 한 줄씩, 문제의 정답을 출력하라.
"""

#????????????????
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    text = input().strip()

    #그냥 스택 담으면서 맨 뒤 3글자 'fox'면 지워
    stack = []
    for alpha in text:
        stack.append(alpha)
         
        if len(stack) >= 3:
            if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                for _ in range(3):
                    stack.pop()

    print(len(stack))