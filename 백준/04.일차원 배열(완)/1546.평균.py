a = int(input())
b = list(map(int, input().split()))
k = max(b)

total = 0

if k == 0:
    print(0.0)  #예외조건

else : 
    for x in b :
        total += (x/k) * 100

print(total / a)