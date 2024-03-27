temperature = input("Enter the temperature : ")

if 'C' in temperature or 'c' in temperature:
    print("The temperature is in Celsius.")
elif 'F' in temperature or 'f' in temperature:
    print("The temperature is in Fahrenheit.")
else:
    print("You should use one of these characters: C, c, F, f")
