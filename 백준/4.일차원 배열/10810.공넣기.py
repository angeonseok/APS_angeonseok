n, m = map(int, input().split())
k = [0] * (n + 1)

for i in range(m) : 
    x, y ,z = map(int, input().split())
    for j in range(x, y+1) :
        k[j] = z

for i in range(1,len(k)):
    print(k[i], end=" ")