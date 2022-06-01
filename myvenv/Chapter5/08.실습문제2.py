a = []

a.append(int(input("1일차 턱걸이 횟수>>>")))
a.append(int(input("2일차 턱걸이 횟수>>>")))
a.append(int(input("3일차 턱걸이 횟수>>>")))
a.append(int(input("4일차 턱걸이 횟수>>>")))
a.append(int(input("5일차 턱걸이 횟수>>>")))
a.append(int(input("6일차 턱걸이 횟수>>>")))
a.append(int(input("7일차 턱걸이 횟수>>>")))


avg = sum(a) / len(a)

print(int(avg))