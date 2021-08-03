# 딕셔너리  / 하나의 변수로 여러개의 값을 다루는 것.
# 데이터 구조화 / 리스트, 딕셔너리, 클래스

# 리스트는 순서(인덱스, index), 딕셔너리 이름(키, key)
list1 = [1,2,3,4]

# key - value
dic1 = {"숫자1" : 1, "숫자2" : 2, "숫자3" : 3, "숫자4" : 4}

# 접근
print(list[0])
print(dic1["숫자3"])

# 딕셔너리 메서드

# 추가
print(dic1)
dic1["숫자5"] = 5
print(dic1)

# 수정
print(dic1)
dic1["숫자5"] = 6
print(dic1)

# 조회
print(dic1["숫자2"])

# 삭제
del dic1["숫자3"]
print(dic1)

# 딕셔너리 - 리스트 사용
# 회원 가능 - 로그인, 회원가입, 중복체크, 비밀번호 찾기
# 회원 - 아이디, 비밀번호, 이름


