# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

n = int(input())
print(n * (n - 1) * (n - 2) // 6) #예시보면 바로 견적나옴
print(3)    #그래도 3차식

