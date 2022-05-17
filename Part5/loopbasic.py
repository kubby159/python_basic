fruits = ["apple","peach","pear"]

for fruit in fruits:
  print(fruit)
  print(fruit+ "Pie")


  # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# sum = 0;
# for n in student_heights:
# 	sum+= n


# print(round(sum/int(len(student_heights))))
total_height = sum(student_heights)
number_of_student = len(student_heights)
result = round(total_height / number_of_student)
print(result)


