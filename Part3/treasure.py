print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


first_question = input("You're at a crossroad. where do you want to go? Type 'left' or 'right' ").lower()
if first_question == 'right':
	print("Fall into a hole. Game Over!")
elif first_question == 'left':
	second_question = input("You've come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'swim' to swim across ").lower()

	if second_question == 'swim':
		print("Attacked by trout. Game Over!")
	elif second_question == 'wait':
		third_question = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colur do you choose? ''').lower()
	
		if third_question == 'red':
			print("Burned by fire. Game Over!")
		elif third_question =='blue':
			print("Eaten by beasts.")
		elif third_question =='yellow':
			print("You win !")
		else:
			print("Game Over!")
		