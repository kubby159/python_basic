# 실습문제
# 사용자로부터 두개의 숫자를 받고, 더한 결과를 출력하기

# x = int(input("첫 번쨰 숫자를 입력하세요>>"))
# y = int(input("두 번째 숫자를 입력하세요>>"))
# print(x+y)

import datetime

# 실습문제2
# 사용자로부터 태어난 연도를 입력받으면, 현재 나이를 출력하기

age = int(input("몇년도에 태어나셨나요?>>"))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
print(f'현재 나이는 {abs(age - year)} 세 입니다.')