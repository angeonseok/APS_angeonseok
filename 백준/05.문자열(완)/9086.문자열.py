a = int(input())
o = []
for _ in range(a) :
    b = input()
    o.append(b[0] + b[-1])

for i in range(len(o)) : 
    print(o[i])