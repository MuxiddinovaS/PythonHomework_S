# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import date

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()
age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day

if age_days < 0:
    age_months -= 1
    age_days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
from datetime import date, timedelta

birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()
next_birthday = date(today.year, birth_month, birth_day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

days_left = (next_birthday - today).days
print(f"Days until your next birthday: {days_left}")

# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

current_date = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Enter meeting duration hours: "))
minutes = int(input("Enter meeting duration minutes: "))

start_time = datetime.strptime(current_date, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
current_tz = input("Enter your current timezone (e.g., Asia/Tashkent): ")
target_tz = input("Enter target timezone (e.g., Europe/London): ")

local_tz = pytz.timezone(current_tz)
target_timezone = pytz.timezone(target_tz)

naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
local_dt = local_tz.localize(naive_dt)
target_dt = local_dt.astimezone(target_timezone)

print("Converted time:", target_dt.strftime("%Y-%m-%d %H:%M"))

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
from datetime import datetime
import time

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    diff = future_time - now
    if diff.total_seconds() <= 0:
        print("Time's up!")
        break
    print(diff)
    time.sleep(1)

# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re

email = input("Enter your email: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email.")
else:
    print("Invalid email.")

# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
phone = input("Enter phone number (digits only): ")
if len(phone) == 10:
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number length.")

# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password)):
    print("Strong password.")
else:
    print("Weak password. Must be at least 8 chars, include uppercase, lowercase, and digit.")

# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
text = """Python is powerful and easy to learn. 
Learning Python can open many opportunities. 
Python developers are in demand."""

word = input("Enter word to find: ").lower()

positions = []
for i, w in enumerate(text.lower().split()):
    if word in w:
        positions.append(i + 1)

print(f"Found '{word}' {len(positions)} times at positions {positions}")

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re

text = input("Enter text: ")
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD format

dates = re.findall(date_pattern, text)
print("Dates found:", dates)
