# 문제 : 자동차 객체를 담을 변수를 만들어주세요.
# 자동차 객체를 변수에 담고 그 변수를 이용해 최고속력이 서로 다르게 만들어주세요.

# 각 자동차가 자신의 최고속력으로 달리게 해주세요.


# 출력 : 자동차가 최대속력 220km로 달립니다.
# 출력 : 자동차가 최대속력 250km로 달립니다.

class Car :

    maxVelo = 0

    def drive(self) :
        print("자동차가 최대속력 {}km로 달립니다.".format(self.maxVelo))

c1 = Car()
c2 = Car()

c1.maxVelo = 220
c2.maxVelo = 250

c1.drive()
c2.drive()
