
print("Let's go learning Korean")
words = ["안녕","반가워","사랑해","고마워"]
total_count = len(words)
correct_count = 0



for word in words:
  print(word)
  answer = input("Please type the word>>>")
  if word == answer:
    correct_count+=1


print(f"전체 문제 개수: {total_count}개")
print(f"맞힌 문제 개수: {correct_count}개")
print(f"틀린 문제 개수: {total_count - correct_count}개")



# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개