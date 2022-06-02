

import random

def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto_number = [] # 로또 번호를 저장할 리스트.

while True:
    x = getRandomNumber()
    if x in lotto_number:
        continue;
    else:
        if len(lotto_number) !=6:
            lotto_number.append(x)
        else:
            break

lotto_number.sort()
for x in lotto_number:
    print(x, end=' ')
        

