import pay_module

# 변수사용
print(pay_module.version)


# 함수 사용
pay_module.printAuthor()



# 클래스 사용

pay_info = pay_module.Pay("A102030", 13000, "2022-06-04")
result =  pay_info.get_pay_info()
print(result)

print(pay_module.__name__)