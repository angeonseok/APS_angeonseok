# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

n = int(input())
print(n*(n-1) // 2) #n(n-1)/2회
print(2)    #n^2