n = int(input())
k = list(map(int, input().split()))
v = int(input())
w = 0

for i in range(n) : 
    if k[i] != v :
        continue
    else :
        w +=1
print(w)