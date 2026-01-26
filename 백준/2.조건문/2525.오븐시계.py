a, b = map(int,input().split())
c = int(input())

a += c // 60 #1시간 넘으면 자동으로 +
b += c % 60 #분은 이래도 그냥 나옴

if b >= 60 :  #60분 이상
    a += 1
    b -= 60
if a >= 24 : #24시 > 0시
    a -= 24

print(a, b)