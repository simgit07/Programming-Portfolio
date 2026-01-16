def c_to_f(c):
    return (c * 9 / 5) + 32


temp = input("Enter temperature (e.g. 25C): ")
celsius = float(temp[:-1])
fahrenheit = c_to_f(celsius)

print(f"{fahrenheit}F")
