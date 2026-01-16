def valid_number(n):
    return 0 <= n <= 100


number = int(input("Enter an integer: "))
print(valid_number(number))
