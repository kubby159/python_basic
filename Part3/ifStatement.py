
# height = int(input("How tall are u?"))
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age=int(input("what is your age?"))
#   if age < 12:
#     bill = 5
#     print("Child tickers are $5.")
#   elif age <=18:
#     bill = 7
#     print("Youth tickers are $7.")
#   else:
#     bill = 12
#     print("Adult tickers are $12.")

#   want_photo = input("Do you want a photo taken? Y or N")
#   if want_photo.upper() =="Y":
#     bill+=3
  
#   print(f"Your final bill is ${bill}.")
  

else:
  print("Sorry, you have to grow taller before you can ride.")


  # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == 'S':
	bill += 15
elif size == 'M':
	bill += 20
elif size == 'L':
	bill += 25


if add_pepperoni == "Y":

	if size == 'S':
		bill+=2
	elif size == 'M' or size == 'L':
		bill+=3


if extra_cheese == 'Y':
	bill+=1


print(f"Your final bill is ${bill}.")