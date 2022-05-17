import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
pick_list = [rock,paper,scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice >=3 or my_choice < 0:
	print("You typed an invalid number, you lose!")
	
else: 
	print(pick_list[my_choice])
	print("Computer chose:")
		# choice_number = random.randint(0,len(computer_choice)-1)


	computer_choice = random.randint(0,len(pick_list)-1)
	print(pick_list[computer_choice])
	if computer_choice == 0 and my_choice == 1:
		print("You Win")
	elif computer_choice == 1 and my_choice == 2:
		print("You Win")
	elif computer_choice == 2 and my_choice == 0:
		print("You Win")
	elif computer_choice == my_choice:
		print("it's a draw:)")
	else:
		print("You Lose!")





