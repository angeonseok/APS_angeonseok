def rev_print(temp) :
    result = temp[::-1]
    return print(result)

def Palind(temp) : 
    if temp == temp[::-1] :
        print('입력하신 단어는 회문(Palindrome)입니다.')

word = input()
rev_print(word)
Palind(word)