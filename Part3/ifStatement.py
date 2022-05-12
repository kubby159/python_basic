
height = int(input("How tall are u?"))
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("what is your age?"))
  if age < 12:
    bill = 5
    print("Child tickers are $5.")
  elif age <=18:
    bill = 7
    print("Youth tickers are $7.")
  else:
    bill = 12
    print("Adult tickers are $12.")

  want_photo = input("Do you want a photo taken? Y or N")
  if want_photo.upper() =="Y":
    bill+=3
  
  print(f"Your final bill is ${bill}.")
  

else:
  print("Sorry, you have to grow taller before you can ride.")