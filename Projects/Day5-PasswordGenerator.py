#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pasw = " "

# for i in range(nr_letters):
#   rd = random.randint(0, len(letters)-1)
#   pasw= pasw + letters[rd]

# for i in range(nr_symbols):
#   rd = random.randint(0, len(symbols)-1)
#   pasw = pasw + symbols[rd]

# for i in range(nr_numbers):
#   rd = random.randint(0, len(numbers)-1)
#   pasw = pasw + numbers[rd]

# print(pasw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pasw=" "
total = nr_letters+nr_numbers+nr_symbols
while len(pasw) <= total:
  rando = random.randint(0,2)
  if rando == 0:
    if nr_letters != 0:
      newrand = random.randint(0, len(letters)-1)
      pasw = pasw + letters[newrand]
      nr_letters=nr_letters-1

  elif rando == 1:
    if nr_numbers != 0:
      newrand = random.randint(0, len(numbers)-1)
      pasw = pasw + numbers[newrand]
      nr_numbers=nr_numbers-1

  else:
    if nr_symbols != 0:
      newrand = random.randint(0, len(symbols)-1)
      pasw = pasw + symbols[newrand]
      nr_symbols = nr_symbols-1
    
print(pasw)