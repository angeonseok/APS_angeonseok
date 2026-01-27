n, m = map(int, input().split())
k = list(range(1, n+1))     #범위 조심

for c in range(m) :
    i, j = map(int, input().split())
    k[i - 1], k[j - 1] = k[j - 1], k[i - 1]     #범위 조심

for i in range(len(k)):
    print(k[i], end=" ")