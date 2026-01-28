# 입력 받은 대로 출력하는 프로그램을 작성하시오.
while 1 :               #예외처리, 무한 입력 무한 출력
    try : 
        a = input()
        print(a)
    except:
        break