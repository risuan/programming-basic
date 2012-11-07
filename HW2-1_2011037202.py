# 주사위 게임 : HW1_2011037202(1.1)
# 주사위를 굴려서 점수를 계산하고 비교하여 승리를 판단한다.
# 입력 : 엔터
# 출력 : 점수와 승리여부.
# 작성자 : 윤세형
# 작성일 : 2011. 09. 22일

import random

#시작
while True :
    start = input('준비가 되셨으면 엔터를 눌러주세요.')

    #게임 규칙을 설명

    if start == '' :
        input('\n주사위 게임에 오신 것을 환영합니다. enter')
    if start == '' :
        print('''
이 게임은 주사위 두 개를 이용해서 높은 점수를 얻은 쪽이 이기게 되는 게임입니다.

- 주사위 두 개를 던졌을 때 두 개 모두 같은 수가 나오면 두 수의 합에다가 2를 곱한 점수를 얻습니다. 그리고 나서 주사위를 한 번 더 던질 수 있습니다. 이 때 같은 수가 한 번 더 나오시면 당신의 승리이지만 그렇지 않고 다른 수가 나왔을 때는 당신이 얻은 점수에서 마지막에 나온 수를 뺍니다.

- 만약 주사위 두 개를 던졌을 때 두 개 모두 같은 수가 나오지 않았다면 한 번 더 던집니다. 이 때 당신은처음 두 수의 합에다가 마지막 수의 반(나머지는 버린)만큼 점수를을 얻을 수 있습니다.''')

        input('\n시작하시겠습니까? 준비가 되셨으면 다시 엔터를 눌러주세요.')

#무작위 주사위 용어 지정
    
    user1 = 1
    user2 = 1
#    user1 = random.randint(1,6)
#    user2 = random.randint(1,6)
    user3 = random.randint(1,6)

    scoreU = (user1+user2)*2
    scoreU2 = (user1+user2)+(user3//2)
    scoreU3 = (user1+user2)*2-user3

    com1 = random.randint(1,6)
    com2 = random.randint(1,6)
    com3 = random.randint(1,6)

    scoreC = (com1+com2)*2
    scoreC2 = (com1+com2)+(com3//2)
    scoreC3 = (com1+com2)*2-com3    

    nextstep = 0
    hResult = 0
    cResult = 0

#사용자 차례
       
    if start == '' :
        print('\n당신의 첫번째 주사위 숫자는' ,user1, '입니다.')
        print('당신의 두번째 주사위 숫자는' ,user2, '입니다.')


    if user1 == user2 :
        more = input('한 번 더 던지겠습니까? Y or N') # 주사위 던지는 여부
        while not((more == 'Y') or (more == 'N')) :
            more = input('다시 입력해주세요.')
        if more == 'Y' : # assert more == 'Y'
            print('\n당신의 세번째 주사위 숫자는' , user3, '입니다.')
            if user1 == user2 and user2!= user3 :
                print('\n당신의 점수는' ,scoreU3, '입니다.')
                hResult = scoreU3
                    
            elif user1 == user2 and user2 == user3 :
                print('\n당신이 승리했습니다. 축하합니다.')
                print('\n\n게임이 끝났습니다. 안녕히 가십시오')
                nextstep = 1
                    
        elif more == 'N' : # assert more == 'N'
            print('\n당신의 점수는' ,scoreU, '입니다.')
            hResult = scoreU
            
                
    elif user1 != user2 :
        print('\n당신의 세번째 주사위 숫자는' ,user3, '입니다.')
        print('\n당신의 점수는' ,scoreU2, '입니다.')
        hResult = scoreU2


    #컴퓨터 차례


    if nextstep == 0 :
        start = input('\n\n이제 컴퓨터의 차례가 되었습니다. enter.')
        if start == '' : # 컴퓨터의 주사위 수
            print('\n컴퓨터의 첫번째 주사위 숫자는' ,com1, '입니다.')
            print('컴퓨터의 두번째 주사위 숫자는' ,com2, '입니다.')
            if com1 != com2 :          
                cResult = scoreC2
                print('\n컴퓨터의 세번째 주사위 숫자는' ,com3, '입니다.')
                print('\n컴퓨터의 점수는' ,scoreC2, '입니다.')
                
            elif com1 == com2 :
                print('\n컴퓨터의 세번째 주사위 숫자는' ,com3, '입니다.')
                if com1 == com2 and com2 == com3 :
                    print('\n컴퓨터의 승리입니다.')
                    print('\n다음에는 좀 더 분발해주십시오.')
                    nextstep = 1
                elif com1 == com2 and com2 != com3 :
                    cResult = scoreC3
                    print('\n컴퓨터의 점수는' ,scoreC3, '입니다.')
            
                
    #점수 비교
    if nextstep == 0 :
        if hResult >= cResult :
            print('\n당신의 승리입니다. 축하합니다.')
            
        elif hResult < cResult :
            print('\n컴퓨터의 승리입니다. 아쉽네요. 다음에는 좀 더 분발해주세요.')
            
    quit = input('게임이 끝났습니다. 게임을 종료하고 싶으시면 q를 눌러주세요.')
    if quit == "q" :
        break
