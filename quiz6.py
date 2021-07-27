# for문을 이용해 list이용하기
list1 = [10,22,33,44,55,66,77,88,99,100]
# 1. len 함수를 이용해 리스트의 길이를 구해주세요.
print(len(list1))
# 2. 구한 길이를 이용해 while문으로 모든 값을 출력해주세요.
i = 0
while i < len(list1) :
  print(list1[i])
  i += 1 
# 3. 위 리스트를 for문을 이용해 출력해주세요.
for aa in list1 :
  print(aa)
# 4. 위 리스트를 for문을 이용해 3의 배수만 출력해주세요.
for aa in list1 :
  if aa % 3 == 0 :
    print(aa)
# 5. 위 리스트를 for문을 이용해 리스트의 모든 값들을 더한 값을 출력해주세요.
s = 0
for aa in list1 :
  s += aa
  print(s)
# while 버전, for .. in 버전

