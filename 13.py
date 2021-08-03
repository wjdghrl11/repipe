# 클래스명 규칙 첫글자는 대문자.
class Dog:
    age = 4
    name = "맥스"
    kind = "푸들"

# 설계도로서, 톨로써 사용하고싶을때
# class Person1:
#     age = 20
#     name = "홍길동"
#     address = "서울"

class Person2:
    age = 22
    name = "홍길순"
    address = "대전"
    #자신이 가진 데이터를 사용할 때는 self라는 매개변수를 사용한다.    
    def introduce(self):
        print("안녕하세요 {}사는 {}살 {}입니다.".format(self.address, self.age, self.name))
# print(Person1.name)
# print(Person2.name)

# 복사본 만들어줘
# 클래스는 설계도,틀이고 객체(인스턴스)는 복사본.
#클래스() 명령어를 이용해 복사본을 생성할 수 있다. 복사본은 이름이 없기 때문에 변수를 이용해 식별
p1 = Person2()
p2 = Person2()
p3 = Person2()
# 리네임 + 데이터를 복사본에 넣어서 정정한다 객체
p2.age = 20
p2.name = "홍길동"
p2.address = "서울"
# 객체
p3.age = 30
p3.name = "임꺽정"
p3.address = "광주"

# print(p1.name)
# print(p2.name)
# print(p3.name)
# 객체의 매서드를 호출하기 위해서는 매서드를 호출하는 주체를 앞에 적어줘야 한다.
# 객체를 이용해 매서드를 호출. 이때 자신의 데이터를 사용할 때는 자신을 인수로 넘기지 않아도 된다 스스토가 데이터를 가지고있기 때문
p2.introduce()
p3.introduce()

list1.append(10) # 매서드 == 함수

#파이썬  > 전부 객체