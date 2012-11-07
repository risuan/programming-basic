# 학번 : 2011037202
# 이름 : 윤세형
''' 프로그램 정보 : member,remove,union,difference,intersection,zip,sprice
각 각을 재귀, 꼬리재귀 while로 짠다.'''

def add(x,xs):
  if member1(x,xs):
    return xs
  else:
    return [x] + xs
  
# 2.1 member, remove 꼬리재귀

def member1(x,xs) : 
  def loop(xs,ss) : 
    if xs == [] : # xs == [] 시 False 출력
      return False
    else : # xs != [] 
      return (x == xs[0]) or loop(xs[1:],add(xs[0],ss)) # x == xs[0]이면 True 출력, 아니면 그 다음 수로 넘어가기
  return loop(xs,[]) # xs 초기화
    

def remove1(x,xs) :
  def loop(xs,rx) :
    if xs == []: # xs == [] 시 False 출력
      return []
    elif x == xs[0] : 
      return rx + xs[1:] # rx에다 xs[1:]을 붙인다.
    else :# xs != [] 
      return loop(xs[1:],add(xs[0],rx)) # x == xs[0]이면 True 출력, 아니면 그 다음 수로 넘어가기
  return loop(xs,[]) # xs 초기화


# 2.2 member ,remove 함수 while 루프

def member2(x,xs) :
  ss = [] # ss 초기화
  while len(xs) >= 0  :
    if xs == [] : # xs == [] 시 False 출력
      return False
    elif x == xs[0] : # x == xs[0]이면 True 출력
      return True
    else : # xs != [] 
      ss = add(xs[0],ss) # ss에 xs[0] 추가
      xs = xs[1:] # xs = xs[1:] 로 다시 지정
      
    
def remove2(x,xs) :
  rx = [] # rx 초기화 
  while len(xs) >= 0 : # xs의 길이가 0이상일동안
    if xs == [] :
      return rx
    elif x == xs[0] : 
      return rx + xs[1:] # rx에다 xs[1:]을 붙인다.
    else :
      rx = add(xs[0],rx) # rx에 xs[0] 추가
      xs = xs[1:] # xs = xs[1:] 로 다시 지정
  return rx
      


# 합집합 재귀, 꼬리, while

def union(a,b) :
  if a == [] or b == []: # a 나 b 가 [] 이면 a+b 를 출력
    return a + b
  else : # a and b != []
    return union(a[1:],add(a[0],b)) # a[1:]로 다시 지정, b에서는 a[0]을 추가

def union1(a,b) :
  def loop(a,b,x) :
    if a == [] or b == []: # a 나 b 가 [] 이면 a+b 를 출력
      return a + b
    else : # a and b != [] 
      return loop(a[1:],add(a[0],b),add(a[0],x)) # a[1:]로 다시 지정, b에서는 a[0]을 추가,x에는 a[0]추가   
  return loop(a,b,[]) # x 초기화

def union2(a,b):
  while len(a) >= 0 : # a의 길이가 0이상이면
    if a == [] or b == [] : # a 나 b 가 [] 이면 a+b 를 출력
      return a + b
    else : # a and b != []
      b = add(a[0],b) # b에서는 a[0]을 추가
      a = a[1:] # a[1:]로 다시 지정
  return b

# 차집합 재귀, 꼬리, while

def difference(a,b) :
  if a == [] : # a == [] 일시 [] 출력
    return []
  elif b == [] : # b == [] 일시 a 출력
    return a
  else : # # a != [] and b!= [] 
    return difference(remove2(b[0],a),b[1:])# b의 맨 앞의 원소 하나 잘라 a에서 찾고 제거, b를 b[1:] 다시 지정
    
    
def difference1(a,b) :
  def loop(a,b,x) :
    if a == [] : # a == [] 일시 [] 출력
      return []
    elif b == [] : # b == [] 일시 a 출력
      return a
    else : # a != [] and b!= [] 
      return loop(remove2(b[0],a),b[1:],add(b[0],x))# b의 맨 앞의 원소 하나 잘라 a에서 찾고 제거, b를 b[1:] 다시 지정
  return loop(a,b,[]) # x 초기화 


def difference2(a,b) :
  while len(b) > 0 : # b의 길이가 0 이상일 동안만
    if a == [] : # a == [] 일시 [] 출력
      return []
    else : # a != [] and b!= []
      a = remove2(b[0],a) # b의 맨 앞의 원소 하나 잘라 a에서 찾고 제거.
      b = b[1:] # b를 b[1:]로 다시 지정
  return a 
    
# 교집합 재귀, 꼬리, while

def intersection(a,b) :
  if len(a) == 0 or len(b) == 0 : # a,b 둘중의 하나의 길이가 0 이면 [] 출력
    return []
  elif a == b : # a == b 되면 a 출력
    return a 
  elif len(a) > len(b) > 0 : # 길이가 a > b 일 때
    if member2(a[0],b) : # b에서 a[0] 존재
      return intersection(a[1:]+a[:1],b) # a[0]을 뒤에 붙이기
    else : # b에 a[0]이 없으면
      return intersection(a[1:],b) # a는 a[1:]로 다시 지정
  else : # a <= b 일 때
    if member2(b[0],a) : # a에서 b[0] 존재
      return intersection(a,b[1:]+b[:1]) # b[0]을 뒤에 붙이기
    else : # a에 b[0]이 없으면
      return intersection(a,b[1:]) # b는 b[1:]로 다시 지정
    
  
def intersection1(a,b) :
  def loop(a,b,x) : 
    if len(a) == 0 or len(b) == 0: # a,b 둘중의 하나의 길이가 0 이면 x 출력
      return x
    elif len(a) > len(b) > 0 : # 길이가 a > b 일 때
      if member2(a[0],b) : # b에서 a[0] 존재하면
        return loop(a[1:],b,add(a[0],x)) # a[0]을 x에 붙이기
      else : # b에서 a[0]이 없을 경우
        return loop(a[1:],b,x) # a = a[1:]
    else : # a<= b
      if member2(b[0],a) : # a에서 b[0] 존재하면
        return loop(a,b[1:],add(b[0],x)) # b[0]를 x에 붙이기
      else : # a에 b[0]이 없을 경우
        return loop(a,b[1:],x) # b = b[1:]
  return loop(a,b,[]) # x 초기화


def intersection2(a,b) :
  x = [] # x 초기화
  if len(a) < len(b) : # 길이가 a<b 일때
    while len(a) > 0 : # a 길이 0이상일 동안
      if member2(a[0],b) : # b에서 a[0] 존재하면
        x = add(a[0],x) # x에 a[0]추가
        a = a[1:] # a = a[1:]로 지정
      else : # b에서 a[0] 없을 경우
        a = a[1:]
    return x
  else : # a >= b
    while len(b) > 0 : # b 길이 0이상일 동안
      if member2(b[0],a) : # a에서 b[0] 존재하면
        x = add(b[0],x) # x에 ㅠ[0]추가
        b = b[1:]
      else : # a에서 b[0] 없을 경우
        b = b[1:]
    return x


# zip sprice 꼬리 함수

def zip1(xs,ys) :
  def loop(xs,ys,ss) :
    if xs == [] or ys == [] : # xs or ys가 0이면
      return ss 
    else : # xs == 0 and ys == 0 
      return loop(xs[1:],ys[1:],add([xs[0],ys[0]],ss)) 
  return loop(xs,ys,[]) # ss 초기화


def sprice1(xs,ys) :
  def loop(xs,ys,ss) :
    if xs == [] and ys == [] : # 둘 다 []이면 출력
      return ss
    elif xs == [] or ys == [] : # 둘 중에 하나가 []이면
      if len(xs) > 0 : # xs 길이가 0이상일때
        return loop(xs[1:],ys,add([(xs[0],xs[0])],ss)) # ss에 xs[0],xs[0] 추가
      elif len(ys) > 0 : # ys 길이가 0이상일때 
        return loop(xs,ys[1:],add([(ys[0],ys[0])],ss)) # ss에 ys[0],ys[0] 추가
    else : # 둘 다 []가 아닐 때
      return loop(xs[1:],ys[1:],add([(xs[0],ys[0])],ss)) # ss에 xs[0],ys[0] 추가
  return loop(xs,ys,[]) # ss 초기화
        

# zip sprice while 함수

def zip2(xs,ys) :
  ss = [] # ss 초기화
  if len(xs) > len (ys) :
    while len(ys) > 0 : # ys 길이가 0이상일때 
      ss = add([(xs[0],ys[0])],ss) # xs[0],ys[0] 추가
      xs = xs[1:] # xs=xs[1:]
      ys = ys[1:] # ys=ys[1:]
    return ss
  else : # xs <= ys 
    while len(xs) > 0 : # xs 길이가 0이상일때
      ss = add([(xs[0],ys[0])],ss) # xs[0],ys[0] 추가
      xs = xs[1:] # xs=xs[1:]
      ys = ys[1:] # ys=ys[1:]
    return ss
      

def sprice2(xs,ys) :
  ss = [] # ss 초기화
  while True :
    if xs == [] and ys == [] : # xs,ys 둘다 []이면
      return ss
      break #  while 끝
    elif xs == [] or ys == [] : # xs,ys 둘 중에 하나만
      if len(xs) != 0 : # xs 길이가 0이 아닐 때
        while len(xs) > 0 : # 0보다 클 동안
          ss = add([(xs[0],xs[0])],ss) #ss에 추가 
          xs = xs[1:] # x= xs[1:]로 지정
      elif len(ys) != 0 : # ys 길이가 0이 아닐 때
        while len(ys) > 0 : # ys 0보다 클 동안
          ss = add([(ys[0],ys[0])],ss) #ss에 추가
          ys = ys[1:] # y = ys[1:]로 지정
    else : # xs,ys 둘 다 [] 이 아닐 경우 
      ss = add([(xs[0],ys[0])],ss) #ss에 추가
      xs = xs[1:]  # xs = xs[1:]로 지정
      ys = ys[1:]  # ys = ys[1:]로 지정
      
            
    
    

