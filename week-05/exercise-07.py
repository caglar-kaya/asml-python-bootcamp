def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
            return num1 / num2
    elif operator == "*":
            return num1 * num2
    else:
        return "Something went wrong!"

print(calculate("a", 7, 5))
