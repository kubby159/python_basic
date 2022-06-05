import csv
import os
from post import Post
file_path = './myvenv/Chapter12/data.csv'

#post 객체를 저장할 리스트
post_list = []

#data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시물 로딩중....")
    file = open(file_path,'r')
    reader = csv.reader(file)
    for data in reader:
        #Post 인스턴스 생성하기
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
#data.csv 파일이 없다면 파일 생성하기.
else:
    file = open(file_path,'w')
    file.close()



print(post_list[0].get_title())