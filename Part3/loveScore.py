# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_name = name1+name2
T = total_name.lower().count("t")
R = total_name.lower().count("r")
U = total_name.lower().count("u")
E = total_name.lower().count("e")


L = total_name.lower().count("l")
O = total_name.lower().count("o")
V = total_name.lower().count("v")
E = total_name.lower().count('e')
					   
					
true_result = T+R+U+E;
love_result = L+O+V+E;
total_result = str(true_result) + str(love_result)
standard_number = int(total_result)

if standard_number < 10 or standard_number > 90:
	print(f"Your score is {total_result}, you go together like coke and mentos.")

elif standard_number > 40 and standard_number < 50:
	print(f"Your score is {total_result}, you are alright together.")

else:
	print(f"Your score is {standard_number}")