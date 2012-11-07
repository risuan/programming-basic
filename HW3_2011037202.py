
# 개발자 정보 : 윤세형 2011037202
# 제작일 : 2011. 10. 13
# 게임 정보 : 섞인 영어 철자를 바로 맞추는 게임


import random



# 게임에서 사용할 단어 목록
WordDB =[
    "abominate","intimidate","provocative","compound","plot","catenation",
    "operation","column","embrass","intensify",
    "conspiracy","breath","bald","consider","resemble","view",
    "corruption","wane","astute","hospitalize","oval","system","letter","problem"]

# 시작메세지 표시
IntroText =  """
+-----------------------------+

  *** 영어 단어 맞추기 게임 ***

 게임에 오신 걸 환영합니다. Enter.

+-----------------------------+
"""
print(IntroText)

# 문제 설명
print('''
이 게임은 섞인 영어 단어를 바로 맞춰보는 게임입니다.
섞인 영어 철자가 제시가 되면 원하는 영어 철자를 원하는 곳에 입력하시면 됩니다.
그럼 시작합니다.
''')

# 목표 점수 입력
Goal = input('목표 점수는 어디까지 하실건가요? : ')
while not Goal.isdigit() :
    Goal = input('목표 점수는 어디까지 하실건가요? : ')
    
# 플레이어 점수 초기화
score1 = 0
score2 = 0

# 매 문제마다 계속 사용하게 될 전역변수 등록
global problemList, problemCandidateList, tryCount , allDone


# 단어를 하나 정해서 문제로 만듬
wordIndex = random.randint(0,len(WordDB)-1)
problemWord = WordDB[wordIndex]

# 글자 리스트를 만듬
problemList = []
for char in list(problemWord) :
    problemList.append( (char,False) ) # (글자, 맞추었는가? )

# 뒤섞은 글자 리스트 만듬
problemCandidateList = list(problemWord)
random.shuffle(problemCandidateList)

# 시도 횟수는 0으로 초기화
tryCount = 0

# 정답 맞춤 플래그 초기화
allDone = False
ending = False

# 플레이어 이름 입력
player1 = input('당신의 이름을 입력해주세요 : ')
player2 = input('상대방의 이름을 입력해주세요 : ')

# 이름이 같으면 다시 입력받기
while player1 == player2 :
    player2 = input('상대방의 이름을 다시 입력해주세요 : ')

# 선행 플레이어 랜덤 돌리기
playerDB = [player1,player2]
Fplayer = random.randint(0,len(playerDB)-1)

 

# 게임 종료시까지 계속반복
while(True) :

    # 현재 플레이어 표시
    if Fplayer == 0 :
        print('\n',player1,'차례입니다.\n')
    elif Fplayer == 1 :
        print('\n',player2,'차례입니다.\n')



    # 시도 횟수 표시
    print ("시도 횟수 :", tryCount)
    
    # 후보 문자 목록 표시
    print ("후보 문자 : ", end="")
    # 후보 문자가 없으면 "없음"으로 표시
    if len(problemCandidateList) <= 0 :
        print ("없음")
        allDone = True
    else :
        for char in problemCandidateList : 
            print (char, "", end="")
        print()
    
    # 문자의 위치번호 표시
    for index in range(len(problemList)) :
        print (str(index) + " ", end="")
    print()
    
    # 현재까지의 맞추기 진행상황 표시
    for char,isRight in problemList :
        if isRight :
            print (char, end="")
        elif char in ["a","e","i","o","u"] :
            print ("?", end="")
        else :
            print ("_", end="")
        print(" ", end="")
    print()
    
    # 정답을 다 맞춘 경우
    if allDone :
        print("축하합니다.")
        print(tryCount, "번 만에 정확히 맞추었습니다.")
        if (score1 and score2) != int(Goal) :
            # 단어를 하나 정해서 문제로 만듬
            wordIndex = random.randint(0,len(WordDB)-1)
            problemWord = WordDB[wordIndex]
            # 글자 리스트를 만듬
            problemList = []
            for char in list(problemWord) :
                problemList.append( (char,False) ) # (글자, 맞추었는가? )
            # 뒤섞은 글자 리스트 만듬
            problemCandidateList = list(problemWord)
            random.shuffle(problemCandidateList)
            # 시도 횟수는 0으로 초기화
            tryCount = 0
            # 정답 맞춤 플래그 초기화
            allDone = False
            continue

            
        cont = input("새 게임을 하려면 엔터키를 눌러주시고, 끝내려면 q를 누른 후 엔터키를 눌러주세요. : ")
        if cont != "q" :
            # 앞에서 한 것처럼 초기화를 함.
            # 단어를 하나 정해서 문제로 만듬
            wordIndex = random.randint(0,len(WordDB)-1)
            problemWord = WordDB[wordIndex]
            # 글자 리스트를 만듬
            problemList = []
            for char in list(problemWord) :
                problemList.append( (char,False) ) # (글자, 맞추었는가? )
            # 뒤섞은 글자 리스트 만듬
            problemCandidateList = list(problemWord)
            random.shuffle(problemCandidateList)
            # 시도 횟수는 0으로 초기화
            tryCount = 0
            # 정답 맞춤 플래그 초기화
            allDone = False
            continue
        else :
            break
   
    input("계속하시겠습니까? 엔터키를 눌러주세요.")
    
    # 글자 입력받음.
    inputChar = input("문자를 선택하세요 : ")
    while(True) :
        # 글자는 후보 문자만 입력받아야 함.
        if inputChar in problemCandidateList :
            break
        inputChar = input("입력이 잘못되었습니다. 문자를 다시 선택하세요 : ")
        
    # 위치값 입력받음.
    inputIndex = input("위치를 선택하세요 : ")
    while(True) :
        if inputIndex.isdigit() : # 위치값은 숫자여야 함.
            inputIndex_int = int(inputIndex)
            if inputIndex_int >= 0 and inputIndex_int < len(problemList) :
                # 위치값은 0 에서 단어길이-1 사이의 값이어야 함.
                break
        inputIndex = input("입력이 잘못되었습니다. 위치를 다시 선택하세요 : ")
    print()
    
    # 입력이 맞았는지 틀렸는지 판단.
    if problemList[int(inputIndex)] == (inputChar,False) :
        print("맞았습니다.")
        problemCandidateList.remove(inputChar)
        problemList[int(inputIndex)] = (inputChar,True)

    # 플레이어와 점수 표시

        if Fplayer == 0 :
            score1 = score1 + 1
            print('\n현재 게임 중인',player1,'은',score1,'점입니다.')
            print(player2,'는',score2,'점입니다.')
        elif Fplayer == 1 :
            score2 = score2 + 1
            print('\n현재 게임 중인',player2,'은',score2,'점입니다.')
            print(player1,'는',score1,'점입니다.')
        
    else :
        print("틀렸습니다.")
    # 플레이어 전환
        if Fplayer == 0 :
            Fplayer = 1
    
        elif Fplayer == 1 :
            Fplayer = 0
        
    # 카운트를 증가시킴.
    tryCount += 1

     # player1의 승리
    if score1 == int(Goal) :
        
        print('\n축하합니다.',player1,'의 승리입니다.')
        cont = input("새 게임을 하려면 엔터키를 눌러주시고, 끝내려면 q를 누른 후 엔터키를 눌러주세요. : ")
        if cont != "q" :
            # 앞에서 한 것처럼 초기화를 함.
            # 단어를 하나 정해서 문제로 만듬
            wordIndex = random.randint(0,len(WordDB)-1)
            problemWord = WordDB[wordIndex]
            # 글자 리스트를 만듬
            problemList = []
            for char in list(problemWord) :
                problemList.append( (char,False) ) # (글자, 맞추었는가? )
            # 뒤섞은 글자 리스트 만듬
            problemCandidateList = list(problemWord)
            random.shuffle(problemCandidateList)
            # 시도 횟수는 0으로 초기화
            tryCount = 0
            # 정답 맞춤 플래그 초기화
            allDone = False

            # 목표 점수 입력
            Goal = input('목표 점수는 어디까지 하실건가요? : ')

            # 플레이어 점수 초기화
            score1 = 0
            score2 = 0

            # 플레이어 이름 입력
            player1 = input('당신의 이름을 입력해주세요 : ')
            player2 = input('상대방의 이름을 입력해주세요 : ')

            # 이름이 같으면 다시 입력받기
            while player1 == player2 :
                player2 = input('상대방의 이름을 다시 입력해주세요 : ')

            # 선행 플레이어 랜덤 돌리기
            playerDB = [player1,player2]
            Fplayer = random.randint(0,len(playerDB)-1)
            


            continue
        else :
            break

    # player2의 승리
    elif score2 == int(Goal) :
        print('\n축하합니다.',player2,'의 승리입니다.')
        cont = input("새 게임을 하려면 엔터키를 눌러주시고, 끝내려면 q를 누른 후 엔터키를 눌러주세요. : ")
        if cont != "q" :
            # 앞에서 한 것처럼 초기화를 함.
            # 단어를 하나 정해서 문제로 만듬
            wordIndex = random.randint(0,len(WordDB)-1)
            problemWord = WordDB[wordIndex]
            # 글자 리스트를 만듬
            problemList = []
            for char in list(problemWord) :
                problemList.append( (char,False) ) # (글자, 맞추었는가? )
            # 뒤섞은 글자 리스트 만듬
            problemCandidateList = list(problemWord)
            random.shuffle(problemCandidateList)
            # 시도 횟수는 0으로 초기화
            tryCount = 0
            # 정답 맞춤 플래그 초기화
            allDone = False

            # 목표 점수 입력
            Goal = input('목표 점수는 어디까지 하실건가요? : ')

            # 플레이어 점수 초기화
            score1 = 0
            score2 = 0

            # 플레이어 이름 입력
            player1 = input('당신의 이름을 입력해주세요 : ')
            player2 = input('상대방의 이름을 입력해주세요 : ')

            # 이름이 같으면 다시 입력받기
            while player1 == player2 :
                player2 = input('상대방의 이름을 다시 입력해주세요 : ')

            # 선행 플레이어 랜덤 돌리기
            playerDB = [player1,player2]
            Fplayer = random.randint(0,len(playerDB)-1)
            
            continue
        else :
            break

    
    



