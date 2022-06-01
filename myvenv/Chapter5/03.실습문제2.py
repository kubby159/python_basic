
study_time = int(input("공부시간을 입력하세요>>>"))
if study_time >= 10:
  print("휴대폰 잠금 해제")
elif study_time >= 5:
  print("휴대폰 30분 사용가능.")
else:
  print("사용불가능.")