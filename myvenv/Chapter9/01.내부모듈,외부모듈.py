# 내장모듈
#: 파이썬 설치 시 자동으로 설치되는 모듈
import math
print(math.pi) # 모듈변수
print(math.ceil(2.8))


from math import pi, ceil
print(pi)
print(ceil(2.1))

from math import pi, ceil as c
print(pi)
print(c(2.1))


# 외부 모듈
# : 다른 사람이 만든 파이썬 파일 pip 로 설치해서 사용
#pyautogui


import pyautogui as pg

pg.moveTo(500,500,duration = 2)