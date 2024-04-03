def calculate_sum(number):
        if number <= 0:
            return 0
        else:
            return number + calculate_sum(number - 1)

print(calculate_sum(10))
