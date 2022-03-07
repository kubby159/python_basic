def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print('You cant drink')
  elif age == 18:
    print('You are new to this!')
  elif age>20 and age< 25:
    print('you are still kind of young')
  else:
    print("enjoy your drink")

age_check(23)

