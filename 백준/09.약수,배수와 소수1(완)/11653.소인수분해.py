# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

#입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

#출력
#N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

n = int(input())
p = []

#상한선. 소인수 분해 목적이면 root n까지해도 ㄱㅊ
limit = int(n ** 0.5) + 1          

# ✅ 에라토스테네스의 체로 소수 리스트 만들기 (빠름)
is_prime = [True] * (limit + 1)             #소수 후보군
if limit >= 0: is_prime[0] = False          #0과 1은 취급안한다
if limit >= 1: is_prime[1] = False

#왜 또 루트거냐? x = a * b 라 하면 a,b는 root x보다 클 수 없다
for i in range(2, int(limit ** 0.5) + 1):   
    if is_prime[i]:
        
        #True면 그놈 배수까지 다 지워버린다                      
        for j in range(i * i, limit + 1, i): 
            is_prime[j] = False

p = [i for i in range(2, limit + 1) if is_prime[i]] #리스트로 모아


n_p = n

for prime in p:
    if prime * prime > n_p:   # 더 이상 나눌 소인수 없음
        break

    while n_p % prime == 0:   # 같은 소인수는 나눠질 때까지 반복
        print(prime)
        n_p //= prime

    if n_p == 1:
        break

if n_p > 1:                 # 마지막에 남는 값이 1이 아니면 그게 소인수(큰 소수)
    print(n_p)