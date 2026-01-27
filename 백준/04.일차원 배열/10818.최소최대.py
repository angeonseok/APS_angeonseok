a = int(input())
n = list(map(int, input().split()))

max_int = n[0]
min_int = n[0]

for i in range(a) : 
    if max_int < n[i] :
        max_int = n[i]
    
    elif min_int > n[i] :
        min_int = n[i]

print(min_int, max_int)