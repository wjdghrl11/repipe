# 논리연산자를 이용해 풀어주세요.
# num이 5보다 크면서 10보다 작을 때 참이 되는 표현을해주세요.
# num이 0보다 작은 경우, 또는 num이 10보다 클 때 참이 되는 표현을해주세요.

num = int(input('숫자를 입력해주세요'))

if num > 5 or num < 10 :
  print('True')
elif num < 0 and num > 10 :
  print('True')
else :
  print('False')  
