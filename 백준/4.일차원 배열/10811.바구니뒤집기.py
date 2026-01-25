n, m = map(int,input().split())
k = [0] * (n+1)

for b in range(1, n+1):
    k[b] = b

for _ in range(m) : 
    i, j = map(int, input().split())
    temp = k[i : j+1]
    temp.reverse()
    k[i:j+1] = temp

for a in range(1, len(k)):
    print(k[a], end=" ")