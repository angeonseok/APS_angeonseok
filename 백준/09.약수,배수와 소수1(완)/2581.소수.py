# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

#출력

m = int(input())
n = int(input())

b = []
p = []

for i in range(m, n+1):
    b.clear()               #매번 초기화해야지
    
    for j in range(1,(int(i ** 0.5) + 1)) : #root i 까지만 범위를 줄이자. n까지 다 하면 너무 걸린다
        if i % j == 0 :
            b.append(j)                     #일단 포함을 시키고
            other = i // j                  #그에 맞는 약수 쌍도 
            if other != j :                 #포함을 시켜야지
                b.append(other)
    
    if len(b) == 2:         #약수 개수가 2개면 > 소수
        p.append(i)         #소수끼리 모아놔

if len(p) == 0:
    print(-1)
else :
    print(sum(p))
    print(p[0])