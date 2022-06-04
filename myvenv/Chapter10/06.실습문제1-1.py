import csv


file = open("./myvenv/Chapter10/mystock.csv",'r')

reader = list(csv.reader(file))

for data in reader[1:]:
    print(f'{data[0]} {(int(data[3])-int(data[1]))*int(data[2])} {round((int(data[3])/int(data[1])-1)*100,2)}%')
    

file.close()