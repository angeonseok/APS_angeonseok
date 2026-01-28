n, m = map(int,input().split())
k = [0] * (n+1)     #0번바구니는 없다

for b in range(1, n+1):
    k[b] = b

for _ in range(m) : 
    i, j = map(int, input().split())
    temp = k[i : j+1]   #슬라이싱 범위 조심
    temp.reverse()
    k[i:j+1] = temp

for a in range(1, len(k)):
    print(k[a], end=" ")