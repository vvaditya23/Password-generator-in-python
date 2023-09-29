#Password Generator Project
import random

#max_length = 12

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
password_str = ""

for char in range(0, 5):
  random_letter = random.choice(letters)
  password.append(random_letter)
  #print(random_letter)

for num in range(0, 5):
  random_number = random.choice(numbers)
  password.append(random_number)

for sym in range(0, 5):
  random_symbol = random.choice(symbols)
  password.append(random_symbol)

random.shuffle(password)
#print(password)

for n in password:
  password_str += n

print(password_str)
