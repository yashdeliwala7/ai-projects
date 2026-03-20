from functions import greet, add_numbers, get_even_numbers, reverse_string, student_score
from api import get_users
import random

# Greeting
name = input("Enter your name: ")
print(greet(name))

# Add numbers
print("Sum:", add_numbers(10, 20))

# Even numbers
numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers:", get_even_numbers(numbers))

# Reverse string
print("Reversed:", reverse_string("python"))

# Student score
print(student_score(name, [80, 90, 85]))

# API + Random User
users = get_users()


if users:
    random_user = random.choice(users)
    print(random_user["name"])
else:
    print("No users found")

print("\nRandom User:")
print(random_user["name"])