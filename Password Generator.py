import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_num = int(input("How many letters would you like in your password? "))
symbol_num = int(input("How many simbols would you like? "))
numbers_num= int(input("How many numbers would you like? "))


password = ""

#Easy
for i in range(1,letter_num+1):
    password+=random.choice(letters)

for i in range(1, symbol_num + 1):
    password += random.choice(symbols)

for i in range(1,numbers_num+1):
    password+=random.choice(numbers)

print(password)

#Hard
chars = list(password)
random.shuffle(chars)
hard_password = "".join(chars)
print(hard_password)