# 파일 저장 및 가져오기

# 파일 저장.
# open("파일경로/파일이름.확장자", "모드")

# 모드 - 텍스트 문서는 t, 그외(이미지, 사운드)는 다 b
# wb - 2진수로 작성
# wt - 문자로 작성
# rb - 2진수로 읽어옴
# rt - 문자로 읽어옴

f1 = open("test.txt", "wt")
# write - 파일에 내용 작성
f1.write("hello\n")
f1.write("bye")
f1.close()

f2 = open("test.txt", "rt")
# read - 파일 내용 전체 읽기
#print(f2.read())

# readline - 파일 내용 한줄씩 읽기
print(f2.readline())
print(f2.readline())

f2.close()

# 이미지 파일 복사 - binary모드 사용
f3 = open("cat.jpg", "rb")

img = f3.read()
f3.close()

f4 = open("newcat.jpg", "wb")
f4.write(img)
f4.close()


# mem1 = {"나이" : 19, "이름" : "홍길동"}
# mem2 = {"나이" : 29, "이름" : "임꺽정"}

# memList = [mem1, mem2]

# age = int(input("사람의 나이를 입력 : "))
# name = input("사람의 이름을 입력 : ")

# mem3 = {"나이" : age, "이름" : name}

# memList.append(mem3)

# print("==== 모든 사람 목록 ====")
# for m in memList :
#     print("나이 : {}".format(m["나이"]))
#     print("이름 : {}".format(m["이름"]))