# 개발자 정보 (윤세형, 2011037202)
# 프로그램에 대한 설명 : 풀그림 만들


def pascal() :
  while True : #control c를 누르기 전까지 반복
    print('''
This program computes combination of two natural numbers, n and r.
Press Control-C to quit.''') # 프로그램 설명
    def comb(n,r) :
      if r == 0 : # r이 0이면 1을 리턴한다.
        return 1
      if r == n :  # r이 n이면 1을 리턴한다.
        return 1
      else :
        s = [1,1] # 2번째 행까지, 1번째 행은 생략
        a = 2 # 2번째까지 만들어져있음으로
        while n + 1 != a : # 재귀를 n번 돌린다.
          s2 = [1,1] # 행을 만들기 위한 기본 틀
          b = 0
          while b + 1 != a : # b + 1 = a가 되는 순간 빠져나온다.
            s2.insert(1,s[b] + s[b+1]) # 전의 행을 이용해 계속 다음 행을 만든다.
            b = b + 1 # 1씩 증가해가며 b + 1 = a가 될 때까지 삽입시킨다. 
          s = s2 # s2를 s에다 저장해준다.
          a = a + 1 # 한 번 돌때마다 1씩 증가
        return s[r] # 원하는 행에서 r번째 있는 값을 출력한다.
    try : # n 값을 받는다.
      n = int(input("Enter n: "))
      assert n >=0 # n의 범위는 0보다 크거나 같다.
    except ValueError : # 숫자가 아닌 것을 입력할때
      print("you should enter a natural number.")
    except AssertionError : # 범위안의 숫자가 아닌 음수를 입력할때
      print("a negative number is not allowed")
    except : # control c를 입력했을때
        print("Good bye")
        break #while 문 끝     
    else :
      try :
        r = int(input("Enter r: "))
        assert n >= r >=0
      except ValueError : # 숫자가 아닌 것을 입력할때
        print("you should enter a natural number.")
      except AssertionError : # 범위안의 숫자가 아닌 음수를 입력할때
        print("a negative number is not allowed")
      except : # control c를 입력했을때
        print("Good bye")
        break #while 문 끝 
       
      else : # 결과값을 출력
        print(n,"C",r,"=",comb(n,r))
        try : # 끝낼 것인지 물어본다.
          End = input("If you want to out, please enter <cnrl>-c : " )
        except : # control c를 입력했을때
          print("Good bye")
          break #while 문 끝 
    
     
    
  
