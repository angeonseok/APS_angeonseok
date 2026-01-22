a, b = map(int,input().split())

if b < 45 :
    if a == 0 :
        a = 23
        b = b + 60
    else :
        a = a - 1
        b = b + 60

print(a, b-45)