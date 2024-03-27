temperature = input("Enter the temperature : ")

if 'C' in temperature or 'c' in temperature:
    print("The temperature is in Celsius.")
    temperature = str(((int(temperature[:-1]) * 9/5)) + 32) + "F"
    print("The temperature is in Fahrenheit now : ", temperature)
elif 'F' in temperature or 'f' in temperature:
    print("The temperature is in Fahrenheit.")
    temperature = str(((int(temperature[:-1]) - 32)) * 5/9) + "C"
    print("The temperature is in Celsius now : ", temperature)
else:
    print("You should use one of these characters: C, c, F, f")
