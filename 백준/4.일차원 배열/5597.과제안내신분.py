s = [0] * 31

for i in (range(28)):
    k = int(input())
    s[k] = 1

for i in range(1, 31) :
    if s[i] == 0:
        print(i)