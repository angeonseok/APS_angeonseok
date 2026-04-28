"""
(0, 0) 에 나이트 말 하나가 놓여 있다. 나이트 말은, (i, j) 위치에서 (i+1, j+2) 혹은 (i+2, j+1) 위치로 움직일 수 있다. 
나이트 말이 (X, Y) 위치에 도달할 수 있는 경우의 수를 109+7 로 나눈 나머지를 출력하라.
 
[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 X,Y정수가 주어진다. (1≤X,Y≤10^6)

[출력]
각 테스트 케이스 마다 문제의 정답을 출력하라
"""

#단순 조합문제인줄
#페르마의 소정리 문제였고

MOD = 10**9 + 7

#팩토리얼 결과를 미리 계산해두기
fac = [1] * (2000001)
for i in range(1, len(fac)):
    fac[i] = (i * fac[i-1]) % MOD

#우선 식을 만족하는 a, b 찾기
def find(X, Y):
    a = 2 * Y - X
    b = 2 * X - Y

    if a % 3 != 0 or b % 3 != 0:
        return -1, -1
    
    return a // 3, b // 3
     
#a, b를 이용한 조합 계산
def sol(X, Y):
    a, b = find(X, Y)
    
    #조합 생성 불가능한 a, b 값 나오면 ㅂㅂ
    if a < 0 or b < 0:
        return 0
    
    n = a + b

    #모듈로 역원 곱셈
    return (fac[n] * pow(fac[a] * fac[b], MOD - 2, MOD)) % MOD 

T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())
    print(f"#{tc} {sol(X, Y)}")