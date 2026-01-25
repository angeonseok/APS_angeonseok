s = input()
asdf = 'abcdefghijklmnopqrstuvwxyz'


for x in asdf : 
    if x in s :
        print(s.index(x), end=" ")
    else : 
        print(-1, end=" ")