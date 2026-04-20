"""
성능이 우수한 보호 필름을 제작하려고 한다.
보호 필름은 [Fig. 1]와 같은 엷은 투명한 막을 D장 쌓아서 제작된다.
막은 [Fig. 1]과 같이 동일한 크기를 가진 바(bar) 모양의 셀들이 가로 방향으로 W개 붙여서 만들어진다.
이렇게 제작된 필름은 두께 D, 가로 크기 W의 보호 필름이라고 한다.

두께 D, 가로크기 W인 보호 필름 단면의 정보와 합격기준 K가 주어졌을 때, 약품 투입 횟수를 최소로 하여 
성능검사를 통과할 수 있는 방법을 찾고,
이때의 약품 투입 횟수를 출력하라. ([Fig. 3] 예제의 경우 정답은 2가 된다.)
약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력한다.

[제약사항]
1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 5초
2. 보호 필름의 두께 D는 3이상 13이하의 정수이다. (3≤D≤13)
3. 보호 필름의 가로크기 W는 1이상 20이하의 정수이다. (1≤W≤20)
4. 합격기준 K는 1이상 D이하의 정수이다. (1≤K≤D)
5. 셀이 가질 수 있는 특성은 A, B 두 개만 존재한다.

[입력]
첫 줄에 총 테스트 케이스의 개수 T가 주어진다.
두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.
각 테스트 케이스의 첫 줄에는 보호 필름의 두께 D, 가로크기 W, 합격기준 K가 차례로 주어진다.
그 다음 D줄에 보호 필름 단면의 정보가 주어진다. 각 줄에는 셀들의 특성 W개가 주어진다. (특성A는 0, 특성B는 1로 표시된다.)

[출력]
테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.
각 줄은 “#x”로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)
출력해야 할 정답은 성능검사를 통과할 수 있는 약품의 최소 투입 횟수이다. 약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력한다.
"""

#1. 체크를 한다.
def check():
    for i in range(w):
        cnt = 1
        for j in range(1, d):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                break
        
        #k개 미만이라 False 반환
        else:
            return False
    
    #전부 다 돌면 True
    return True


#2. 약품 투여를 한다.
def injcet(row, cnt):
    global ans

    #가지치기    
    if cnt >= ans:
        return
    
    #성능검사 통과하면 정답 갱신
    if check():
        ans = min(ans, cnt)
    if row == d:
        return 
    
    cur_row = arr[row][:]

    #1. 걍 간다
    injcet(row+1, cnt)

    #2. A 투여한다
    arr[row] = [0] * w
    injcet(row+1, cnt+1)

    #3. B 투여한다
    arr[row] = [1] * w
    injcet(row+1, cnt+1)

    arr[row] = cur_row 


T = int(input())
for tc in range(1, T + 1):
    d, w, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(d)]

    ans = d
    
    if check():
        ans = 0
    
    else:
        injcet(0,0)

    print(f"#{tc} {ans}")