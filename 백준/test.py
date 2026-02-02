t = 10
for i in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for j in range(2, n-1):
        lf = 0
        ri = 0
        m = 0

        l2 = a[i-2]
        l1 = a[i-1]
        r1 = a[i+1]
        r2 = a[i+2]

        if l2 > l1 :
            lf = l2
        else:
            lf = l1

        if r2 > r1:
            ri = r2
        else:
            ri = r1

        if lf > ri:
            m = lf
        else:
            m = ri

        if a[i] > m :
            ans += a[i]-m
        
    print(f'#{i} {ans}')