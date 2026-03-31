"""
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다. 만약에 1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

#입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.
입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

#출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.
"""

MOD = 1000000007

#클래스가 아닌 함수로 정의함
#곱셈 결과들은 전부 MOD로 나눠줌
def build(arr, node, start, end):
    if start == end:
        tree[node] = arr[start] % MOD
    else:
        mid = (start + end) // 2
        build(arr, node * 2, start, mid)
        build(arr, node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def update(node, start, end, idx, val):
    if start == end:
        tree[node] = val % MOD
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(node * 2, start, mid, idx, val)
        else:
            update(node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[node] % MOD
    
    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) * query(node * 2 + 1, mid + 1, end, left, right)) % MOD

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
N = len(arr)
tree = [0] * (4 * N)
build(arr, 1, 0, N-1)

for _ in range(m + k):
    cmd, b, c = map(int, input().split())

    if cmd == 1:
        update(1, 0, N-1, b-1, c)
        
    elif cmd == 2:
        mul_num = query(1, 0, N-1, b - 1, c - 1)
        print(mul_num)