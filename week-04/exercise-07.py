first_side = input("Enter the first side : ")
second_side = input("Enter the second side : ")
third_side = input("Enter the third side : ")

first_side = float(first_side)
second_side = float(second_side)
third_side = float(third_side)

isValid = first_side + second_side > third_side
            and first_side + third_side > second_side
            and second_side + third_side > first_side

if isValid:
    if first_side == second_side and first_side == third_side:
        print("Your triangle is equilateral")
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        print("Your triangle is isosceles")
    else:
        print("Your triangle is scalene")
else:
    print("This cannot form a triangle")
