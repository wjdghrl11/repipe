# def gugudan(dan) :
 
#   i = 1
#   while i <= 9 :
#       if i == 5:
#           return
#       print("{} * {} = {}".format(dan, i, dan * i))
#       i += 1
def square(num) :
  return num * num

# 제곱한 값에다가 추가적인 연산
a = aquare(5)
print("a : {}".format(a / 2))

a = square(5)
print("a : {}".format(a * 2))
#   return # 돌아가라 함수끝내기
# 리턴을하면 함수호출을 한값이 리턴값으로 변한다

# 함수를 사용하는 이유
# 1. 코드의 재활용
# 2. 코드의 구조화
# 3. 코드의 집중화 - 지역/전역