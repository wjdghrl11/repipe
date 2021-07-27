# 1 ~ 10 까지 수 리스트 선언
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
# 리스트 값 짝수만 가져오기
print(list1[0])
print(list1[1])
print(list1[3])
print(list1[5])
print(list1[7])
print(list1[9])

i = 0
while i < 10 :
  if list1[i] % 2 == 0 :
    print(list1[i])
  i += 1

# 리스트에 11,13,15 추가하기
list1.append(11)
list1.append(13)
list1.append(15)
print(list1)
# 리스트의 짝수번째 값 1증가시키기
list1[0] += 1
list1[2] += 1
list1[4] += 1
list1[6] += 1
list1[8] += 1
list1[8] += 1
print(list1)

i = 0

while i < 13 : 
  if i % 2 == 0 :
    list1[i] += 1
  i += 1
# 리스트에서 세번째 값 지우기
del list1[2]
print(list1)