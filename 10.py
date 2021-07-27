# 리스트
list1 = [1,2,3,4,5] 
print(list1[0]) 

# 리스트 사용법 - 객체의 일종. 
# 리스트 다수의 데이터를 효율적으로 저장하고 관리 추가, 조회, 수정, 삭제

# 1. 가장 뒤에 추가 .append(값)
print(list1)
list1.append(6) # 주체를 앞에붙이고 뒤에붙인다
print(list1) # 다시 출력

# 원하는 위치에 추가 - insert(위치, 값)
list1.insert(0, 7)
print(list1)

# 리스트 합치기 - extend(추가할 객체)
list2 = [1,2,3]
list3 = [4,5,6]

list2.extend(list3)
print(list2)

# 수정 - 수정을 원하는 인덱스 선택후 대입으로 수정
list2[2] = 100
print(list2)

# 조회
print(list2[2]) # 조회를 원하는 인덱스로 선택후 사용.

# 삭제

# 원하는 위치 삭제
del list2[2]
print(list2)

# 마지막 삭제
list2.pop()
print(list2)

# 원하는 값으로 삭제
list2.remove(4) # 리스트의 4를 찾아서 삭제해줌
print(list2)
# 전체 삭제
list2.clear()
print(list2)