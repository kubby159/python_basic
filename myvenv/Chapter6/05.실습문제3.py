import random

def getRandomNumber():
    number = random.randint(1,45)
    return number



def make_lotto_number():
    lotto_number = [] # 로또 번호를 저장할 리스트.
    while True:
        x = getRandomNumber()
        if x not in lotto_number:
            lotto_number.append(x)
        if len(lotto_number) > 5:
                break
        else:
                continue
    lotto_number.sort()
    return lotto_number

for i in range(5):
    print(make_lotto_number())
    



            





