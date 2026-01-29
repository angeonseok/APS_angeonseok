#nCm 계산해보자

#입력
#첫째 줄에 N과 K가 주어진다.

#출력
#nCk

n, k = map(int,input().split())

def fac(i):                     #팩토리얼 있어야한다
    if i == 0:
        return 1
    else :
        return i * fac(i-1)

print(int(fac(n) / (fac(k) * fac(n-k))))        #조합 공식임