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


# 게시글 쓰기
def write_post():
    ''' 게시글 쓰기 함수'''
    print('\n\n - 게시글 쓰기 -')
    title = input("제목을 입력해 주세요.\n>>>")
    content = input("내용을 입력해 주세요.\n>>>")
    # 글번호
    id = post_list[-1].get_id()+1
    post = Post(id, title,content,0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

# 게시글 목록
def list_post():
    '''게시글 목록 보기 함수''' 
    print("\n\n- 게시글 목록 - ")   
    id_list = []
    for x in post_list:
     
        print(f'번호 : {x.get_id()}')
        print(f'제목 : {x.get_title()}')
        print(f'조회수 : {x.get_view_count()}')
        print('')
        id_list.append(x.get_id())

    while True:
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            id = int(input('>>>'))   
            if id in id_list:
                detail_post(id)
                break
                    
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

#글 상세 페이지
def detail_post(id):
    ''' 게시글 상세 보기 함수'''
    print("\n\n- 게시글 상세 -")
    for post in post_list:
        if id == post.get_id():
            #조회수 1증가
            post.add_view_count()
            print(f"번호 : {post.get_id()}")
            print(f'제목: {post.get_title()}')
            print(f'본문: {post.get_content()}')
            print(f'조회수: {post.get_view_count()}')
            target_post = post
    
    while True:
        print('Q) 수정 : 1 삭제: 2 (메뉴로 돌아가려면 -1 을 입력)')
        try:
           choice = int(input(">>>"))
           if choice == 1:
               update_post(target_post)
               break
           elif choice == 2:
                delete_post(target_post)
                break
           elif choice == -1:
                break
           else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

# 게시글 수정
def update_post(target_post):
    ''' 게시글 수정 함수'''
    print('\n\n- 게시글 수정 -')
    t = input("제목을 입력해주세요\n >>>")
    c = input("본문을 입력해주세요\n >>>")
    target_post.set_post(target_post.id, t, c, target_post.view_count)
    print("# 게시글이 수정되었습니다.")

# 게시물 삭제
def delete_post(target_post):
    ''' 게시글 삭제 함수'''
    post_list.remove(target_post)

# 게시글 저장
def save():
    ''' 게시글 저장 함수'''
    f = open(file_path, 'w')
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("저장이 완료되었습니다.")
    print("프로그램 종료")
# 메뉴 출력하기
while True:
    print('\n\n - FASTCAMPUS BLOG -')
    print("- 메뉴를 선택해 주세요. -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input('>>>'))
    except ValueError:
        print("숫자를 입력해 주세요.")
    else:
        #try 부분에서 오류가 발생하지 않았다면 아래 코드 실행.
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            save()
            break


print(post_list)