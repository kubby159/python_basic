# 함수를 사용하는 이유

# 함수를 사용하지 않는 경우
print("안녕하세요. 동준님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")
print("안녕하세요. 현식님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")
print("안녕하세요. 원준님")
print("현재 프리미엄 서비스 사용기간이 23일 남았습니다.")


# 함수를 사용한 경우
def printMessage(name,date):
    print(f"안녕하세요. {name}님")
    print(f"현재 프리미엄 서비스 사용기간이 {date}일 남았습니다.")



printMessage("동준",30)
printMessage("현식",7)
printMessage("원준",23)


# 함수의 기본 형태
''' 
def 함수이름 (매개변수1,매개변수2):
    명령블록.

    호출하기()
'''
