# ====================== Temprature converter ========================

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")
else:
    print("Invalid choice")



# ====================  TO-DO =================

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    print("Current tasks:")
    for task in tasks:
        print(task)

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid input")


# ===================  calculate_bmi =============

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight")
elif 25 <= bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese")





# ==============  Currency Converter  ===============

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

currencies = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.36,
}

print("Available currencies:")
for currency in currencies:
    print(currency)

from_currency = input("Enter the currency you have (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
amount = float(input(f"Enter the amount in {from_currency}: "))

if from_currency in currencies and to_currency in currencies:
    exchange_rate = currencies[to_currency] / currencies[from_currency]
    result = convert_currency(amount, exchange_rate)
    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
else:
    print("Invalid currency input")


# ============= randome password genarateor ================

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter the length of the password: "))
password = generate_password(length)

print(f"Generated password: {password}")


#===========  word-Counter  ============
def count_words(text):
    words = text.split()
    return len(words)

text = input("Enter a sentence or paragraph: ")
word_count = count_words(text)

print(f"The text contains {word_count} words.")
