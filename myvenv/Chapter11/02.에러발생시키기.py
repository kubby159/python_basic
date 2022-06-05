# raise 구문을 사용해서 에러를 강제로 발생시켜 보자.

try:
    num = int(input("음수를 입력해 주세요>>"))

    if num >=0:
        raise ValueError("양수는 입력 불가")
except Exception as e:
    print(f"에러 발생! {e}")