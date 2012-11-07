# 프로그램 정보 : 각각의 곱셈을 함수로 만든다.
#1. 단순무식한 곱셈 함수 2. 빠른 곱셈 함수 3. 러시안 농부의 곱셈함수
# 이름 : 윤세형
# 학번 : 2011037202


# 단순무식한 곱셈 함수 : 곱셈을 재귀를 이용해서 계속 더해주는 형식으로 함수를 만든다.


def mult1(m,n) :
  if m >= 0 and n >= 0 :
  #꼬리재귀형태
    def loop(n,ans) :
      if n == 0 : # 최종 값 리턴
        return ans
      else : # n = 0 일때까지 반복
        return loop(n-1,m+ans)
    return loop(n,0)
  else:
    print('다시 입력해주세요.')

def mult2(m,n) :
  #while문 형태
  if m >= 0 and n >= 0 :
    ans = 0
    while n > 0 : # n이 0이상인 동안만 작동
      ans = m + ans # ans에 계속 m을 더해준다.
      n = n - 1
    return ans
  else :
    print('다시 입력해주세요.')


# 빠른 곱셈 함수 : 두 함수 double과 halve를 이용하여
# 곱셈함수의 덧셈을 하는 회수가 log n에 비례하는 곱셈함수 multfast를 작성한다.



def double(n) : # double 함수
    return n * 2
def halve(n) : # halve 함수
    return n // 2
  
def multfast(n,m) :
  # 재귀함수형태
  if m > 0 and n > 0 : # m과 n 모두 양수로만 받는다.
    if m == 1 : # n = 1 일때 결과값을 리턴
      return n
    elif m % 2 == 0 : # 2로 나눈 m의 나머지가 0일 때 
      return multfast(double(n),halve(m)) 
    else : # 2로 나눈 m의 나머지가 0이 아닐 때
      return multfast(n,m-1) + n # n을 계속 더해준다.
  else :
    print('다시 입력해주세요.')
  

def multfast1(a,n) :
  # 꼬리재귀함수형태
  if a > 0 and n > 0 : # 입력받는 두 수 모두 양수로만
    def loop(a,n,r) :
      if n == 0 : # n이 0일 떄 결과값을 리턴
        return r
      elif n % 2 == 0 : # 2로 나눈 m의 나머지가 0일 때
        return loop(double(a),halve(n),r)
      else : # 2로 나눈 m의 나머지가 0이 아닐 때
        return loop(a,n-1,a+r) # r에다 계속 a를 더해준다.
    return loop(a,n,0)
  else :
    print('다시 입력해주세요.')
    
def multfast2(a,n) :
  if a > 0 and n > 0 : # 입력받는 두 수 모두 양수로만
    ans = 0
    while n >0 : # n이 0 이상인 동안만 작동
      if n % 2 == 0 :
        a = double(a)
        n = halve(n)
      else :
        n = n-1
        ans = a + ans # ans에 a를 계속 더해준다.
    return ans
  else :
    print('다시 입력해주세요.')

def multRP(n,m) :
  if n > 0 and m > 0 : # n,m 두 수 모두 양수
    if m == 1 : # m이 1일 때 결과값을 리턴
      return n  
    elif m % 2 == 0 : # m을 2로 나눈 값의 나머지가 0일 때
      return multRP(2*n,m/2)
    else : # m을 2로 나눈 값의 나머지가 0이 아닐 때
      return multRP(2*n,m//2) + n # 계속 n을 더해간다.
  else :
    print('다시 입력해주세요.')

def multRP1(n,m) :
  if n > 0 and m > 0 : # n,m 두 수 모두 양수
    def loop(n,m,r) :
      if m == 1 : # m이 1일 때 결과값을 리턴
        return n + r
      elif m % 2 == 0 : # m을 2로 나눈 값의 나머지가 0일 때
        return loop(2*n,m/2,r)
      else :
        return loop(2*n,m//2,n+r) # r의 값에다 계속 n을 더해간다.
    return loop(n,m,0)
  else :
    print('다시 입력해주세요.')
  
 
    

# 3. multRP와 multfast 함수 성능 비교
# 만약 뒤의 수가 2^n일 경우 예시를 들어 (8.16)이면 multRP와 multfast의 덧셈 횟수는 0으로 같고, 사용공간 5줄로 같다.
# 하지만 뒤의 수가 2^n이 아닐 경우 예시를 들면 (8.15)이면 multRP와 multfast의 덧셈 횟수는 4로 같다. 그러나 사용공간은 multfast일 경우
# 7줄, multRP의 경우 4줄로 mult RP가 훨씬 적다.
# 뒤의 수가 홀수가 아니고 2^n도 아닌 그냥 짝수인 경우 예시를 들면 (8,18)이면 multfast와 multRP의 덧셈횟수는 역시 같다.
# 그러나 사용공간은 multfast일 경우 6줄, multRP일 경우 5줄로 마찬가지로 multRP이 적은 걸 볼 수 있다.
# 따라서 두 함수의 덧셈 횟수는 같으나 multRP이 사용공간이 multfast보다 어느 경우에서도 같거나 적은 걸 볼 수 있음으로 multRP가 성능이 좋다.
