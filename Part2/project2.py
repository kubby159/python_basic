#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#first

print("Welcome to the tip calculator.")
total_bill = float(input("what was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

head_counter = int(input("How many people to split the bill? "))

except_tip = total_bill + (total_bill * (tip_percentage/100))

result = round((except_tip / int(head_counter)) , 2)
print(f"${result}")

# result = (float(total_bill) * float(tip_percentage/100)) / int(head_counter)

# print(f"Each person should pay: {float(result)}")