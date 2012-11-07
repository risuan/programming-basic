
# 주사위 게임2 : HW2_2011037202
# 주사위를 굴려서 수를 맞추는 게임입니다.
# 입력 : 숫자
# 출력 : 판단여부.
# 작성자 : 윤세형
# 작성일 : 2011. 09. 29일

enter = input('\n주사위 게임에 오신 것을 환영합니다.')

#주사위 던지기
import random

D1 = random.randint(1,6)
D2 = random.randint(1,6)
count = 0

#엔터를 눌러주시와요.
if enter == '' :
    print(" 이 게임은 주사위 한쌍의 수를 맞추는 게임입니다.")

#q를 누르지 않는 이상 무한 게임
while True :
    N1 = input('''\n게임을 시작합니다.첫번째 주사위 수를 알아맞춰보세요. 만약 그만하고 싶으시다면 언제든지 q를 눌러주세요.''')
    if N1 == 'q' :
        #q가 나오면 종료
        print("\n게임이 끝났습니다. 안녕히 가십시오.")
        break;
    #어떤 입력을 받아도 죽지 않게
    while not N1.isdigit() or int(N1)>7 or int(N1)<0 :
        if N1 == 'q' :
            print("\n게임이 끝났습니다. 안녕히 가십시오.")
            break;
        N1 = input("다시 입력해주세요.")

    #첫번째 주사위 맞추기
    if N1 != 'q' :
        
        while True :
            while not N1.isdigit() or int(N1)>7 or int(N1)<0 :
                if N1 == 'q' :
                    break;
                print("\n게임이 끝났습니다. 안녕히 가십시오.")
                N1 = input("다시 입력해주세요.")
            N1 = int(N1)
            if int(N1) < D1 :
                N1 = input("\nUP")
                count = count + 1
            elif int(N1) > D1 :
                N1 = input("\nDOWN")
                count = count + 1
            else : #N1 == D1
                count = count + 1
                print('''정답입니다.''', count ,'''만에 맞추셨습니다.''')
                break;

    #언제든지 종료
    if N1 =='q' :
        break;

    N2 = input('''\n이번에는 두번째 주사위 수를 알아맞춰보세요. 만약 그만두고 싶으시면 언제든지 q를 눌러주세요.''')
    count = 0
    if N2 == 'q' :
        #q가 나오면 종료
        print("\n게임이 끝났습니다. 안녕히 가십시오.")
        break;
    while not N2.isdigit() or int(N2)>7 or int(N2)<0 :
            N2 = input("다시 입력해주세요.")
            if N2 == 'q' :
                print("\n게임이 끝났습니다. 안녕히 가십시오.")
                break;
            
    #두번째 주사위 맞추기    
    if N2 != 'q' :
        
        while True :
            while not N2.isdigit() or int(N2)>7 or int(N2)<0 :
                if N2 == 'q' :
                    print("\n게임이 끝났습니다. 안녕히 가십시오.")
                    break;
                N2 = input("다시 입력해주세요.")
            if N2 == 'q' :
                break;
            N2 = int(N2)
            if int(N2) < D2 :
                N2 = input("\nUP")
                count = count + 1
            elif int(N2) > D2 :
                N2 = input("\nDOWN")
                count = count + 1
            else : #N2 == D2
                count = count + 1
                print('''정답입니다.''', count ,'''만에 맞추셨습니다.''')
                break;

    #언제든지 종료
    if N2 =='q' :
        break;
    
#게임이 완전히 끝났을 때
    quit = input("\n게임이 끝났습니다. 종료를 원하시면 q를 눌러주세요.")
    if quit == 'q' :
        print('\n게임이 끝났습니다. 안녕히 가십시오.')
        break

    
