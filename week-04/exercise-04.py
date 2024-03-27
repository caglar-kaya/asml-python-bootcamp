numbers = []

first_number = input("Enter the first number : ")
numbers.append(int(first_number))

second_number = input("Enter the second number : ")
numbers.append(int(second_number))

third_number = input("Enter the third number : ")
numbers.append(int(third_number))

print("Your smallest number is ", min(numbers))
print("Your largest number is ", max(numbers))
