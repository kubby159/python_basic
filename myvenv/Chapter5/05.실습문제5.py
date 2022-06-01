
mother_tongue = int(input("국어>>>"))
math = int(input("수학>>>"))
english = int(input("영어>>>"))

score_average = (mother_tongue+math+english)/3

#방법2
if mother_tongue < 0 or math < 0 or english < 0 or mother_tongue > 100 or math > 100 or english > 100:
  print("잘못 입력했습니다.")
elif score_average >=80 :
  print("불합격")
else:
  print("합격")


# 방법1
if 0<= mother_tongue <= 100 and 0<=math <=100 and 0 <=english<=100:
  if score_average >= 80:
    print("합격")
  else:
    print("불합격")
else:
  print("잘못 입력하였습니다.")