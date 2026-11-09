import random
import string
print ("hello to the Email maker")
random_letters = "".join(random.choices(string.ascii_letters, k=10))
email=("@gmail.com")
birth_year = int(input("Enter your birth year:  "))
random_num = random.randint(10, 99999999)
if birth_year <= 2011:
  print((random_letters)+ str(birth_year) + str(random_num) + email)

  


else:
    print("age to small pls try again")