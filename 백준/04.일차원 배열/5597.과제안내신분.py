s = [0] * 31 #0번인덱스는 뺴고 총 30개 해야지

for i in (range(28)):
    k = int(input())
    s[k] = 1

for i in range(1, 31) :
    if s[i] == 0:
        print(i)