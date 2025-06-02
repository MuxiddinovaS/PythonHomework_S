#Write a Python program to ask for a user's name and year of birth, then calculate and display their age
from datetime import datetime

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")
#Extract car names from the following text:

txt = 'LMaasleitbtui'
txt[::2]
txt[1::2]
#Extract car names from the following text:

txt = 'MsaatmiazD'
txt[-1::-2]
txt[::2]

#Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt = "I'am John. I am from London"

if "I am from" in txt:
    residence = txt.split("I am from")[1].strip()
    print("Residence area:", residence)
else:
    print("Residence area not found.")
#Write a Python program that takes a user input string and prints it in reverse order.
user_input= input("Enter a string:")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

#Write a Python program that counts the number of vowels in a given string.
given_string = input("Enter a string")

vowels = 'auioe'

cnt = 0

for i in given_string:
    if i.lower() in vovels:
        cnt = cnt + 1

cnt
#Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = input("Enter numbers separated by spaces: ")
number_list = list(map(int, numbers.split()))
max_value = max(number_list)

print("Maximum value:", max_value)

#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Enter a word: ")
word = word.lower()
if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
#Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email address: ")
if "@" in email:
    domain = email.split('@')[1]
    print("Domain:", domain)
else:
    print("Invalid email address.")
#Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string
password_length = int(input("Enter desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))

print("Generated password:", password)

