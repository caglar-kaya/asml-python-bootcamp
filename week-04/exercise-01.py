age = input("Enter your age : ")

if int(age) > 18:
    print("You can vote!")
else:
    print("You can not vote!")

print("You can vote!" if int(age) > 18 else "You can not vote!")
