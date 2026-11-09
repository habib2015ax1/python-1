import random

print ("hello to the Email maker")
First_name=input("enter your first name: ")
last_name=input("Enter your last name: ")
dash=("_")
email=("@gmail.com")
birth_year = int(input("Enter your birth year:  "))
random_num = random.randint(10, 99999999)
if birth_year <= 2010:
  print(First_name+  dash + last_name + str(birth_year) + str(random_num) + email)

  


else:
    print("age to small pls try again")