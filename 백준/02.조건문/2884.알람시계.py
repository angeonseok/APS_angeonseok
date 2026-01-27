a, b = map(int,input().split())

if b < 45 :    #시 단위 변동
    if a == 0 :
        a = 23
        b = b + 60
    else :      #그 외
        a = a - 1
        b = b + 60

print(a, b-45)