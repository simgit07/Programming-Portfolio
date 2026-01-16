def to_binary(n):
    return bin(n)[2:]


# Test program
number = int(input("Enter a positive integer: "))
print("Binary:", to_binary(number))
