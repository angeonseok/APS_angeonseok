"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열

#입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

#입력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

#주어진 리스트로 순열을 만든다
def perm(depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        path.append(arr[i])

        perm(depth + 1)

        visited[i] = False
        path.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()      #사전순 맞추기 위해 정렬

visited = [False] * n
path = []
perm(0)