# First solution:

favorite_drink = input("Please enter your favorite drink: ")

print(f"I also like {favorite_drink}, what a coincidence!")

# Second solution:

import sys

def enter_your_favorite_drink():
	if len(sys.argv) > 1:
		print(f"I also like {sys.argv[1]}, what a coincidence!")
	else:
		print("Usage: python script.py [your favorite drink]")

enter_your_favorite_drink()

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

print(f"Sum of two number is :: {num_1 + num_2}")
