n, m = map(int, input().split())
k = [0] * (n + 1)   #0번바구니는 없다

for i in range(m) : 
    x, y ,z = map(int, input().split())
    for j in range(x, y+1) :    #range 범위 조심
        k[j] = z

for i in range(1,len(k)):   #0번바구니는 없다
    print(k[i], end=" ")