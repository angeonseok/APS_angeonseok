"""
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.
여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

#입력
첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.

#출력
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.
"""

#세그먼트 트리인데 업데이트 필요없음
import sys
input = sys.stdin.readline

#최댓값 세그먼트 트리
class MaxSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        self.build(arr, node * 2, start, mid)
        self.build(arr, node * 2 + 1, mid + 1, end)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return -10**18      #연산에 영향을 주지 않게 

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return max(
            self._query(node * 2, start, mid, left, right),
            self._query(node * 2 + 1, mid + 1, end, left, right)
        )

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

#최소값 세그먼트 트리
class MinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        self.build(arr, node * 2, start, mid)
        self.build(arr, node * 2 + 1, mid + 1, end)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 10**18       #연산에 영향을 주지 않게 

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return min(
            self._query(node * 2, start, mid, left, right),
            self._query(node * 2 + 1, mid + 1, end, left, right)
        )

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

st_max = MaxSegmentTree(arr)
st_min = MinSegmentTree(arr)

for _ in range(m):
    a, b = map(int, input().split())
    print(st_min.query(a - 1, b - 1), st_max.query(a - 1, b - 1))