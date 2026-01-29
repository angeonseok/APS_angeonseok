# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#입력
#첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

#출력
#주어진 수들 중 소수의 개수를 출력한다.

a = int(input())
num_a = list(map(int, input().split()))
b = []
p = 0

for i in num_a:
    b.clear()               #매번 초기화해야지
    
    if i < 2 :              #1은 나가라
        continue
    
    for j in range(1,i+1) : #약수들을 모으고
        if i % j == 0 :
            b.append(j)
    
    if len(b) == 2:         #약수 개수가 2개면
        p += 1              #소수 개수가 1개 늘어야지

print(p)


# # ✅ 에라토스테네스의 체로 소수 리스트 만들기 (빠름)
# is_prime = [True] * (limit + 1)             #소수 후보군
# if limit >= 0: is_prime[0] = False          #0과 1은 취급안한다
# if limit >= 1: is_prime[1] = False

# for i in range(2, int(limit ** 0.5) + 1):    #왜 또 루트거냐? x = a * b 라 하면 a,b는 root x보다 클 수 없다
#     if is_prime[i]:                          #False면 이미 다 죽었어
#         for j in range(i * i, limit + 1, i): #True면 그놈 배수까지 다 지워버린다
#             is_prime[j] = False

# p = [i for i in range(2, limit + 1) if is_prime[i]] #리스트로 모아