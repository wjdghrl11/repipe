# 어떤 차의 높이가 170cm 입니다..

# 이 차는 3개의 터널을 차례대로 지나게 될 것입니다.

# 터널의 높이가 차의 높이보다 같거나 낮다면 차는 터널과 충돌하여 사고가 납니다.

# 터널의 높이를 순서대로 3개 입력한 후 터널을 무사히 잘 통과하면 PASS 를 출력하고, 사고가 난다면 CRASH 를 출력하세요.

# 예시 ) tunel1 = 162
#        tunel2 = 180
#        tunel3 = 166

# 터널의 높이가 위와 같다면 tunel1과 tunel3에서 걸리므로 CRASH
# '''

# car = 170

# ## 입출력 예시
# # 첫번째 터널의 높이를 정해주세요 : 177
# # 두번째 터널의 높이를 정해주세요 : 166
# # 세번째 터널의 높이를 정해주세요 : 182
# # CRASH


# # 첫번째 터널의 높이를 정해주세요 : 177
# # 두번째 터널의 높이를 정해주세요 : 173
# # 세번째 터널의 높이를 정해주세요 : 180
# # PASS

car = 170
tunel = int(input("첫번째 터널의 높이를 정해주세요 : "))
tunel2 = int(input("두번째 터널의 높이를 정해주세요 : "))
tunel3 = int(input("세번째 터널의 높이를 정해주세요 : "))

if tunel <= car :
  print("Crash")

elif tunel2 <= car :
  print('crash') 

elif tunel3 <= car : 
  print('crash') 
  
else :
  print("pass")  