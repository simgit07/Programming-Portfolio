def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


s = input("Enter a string: ")
u, l = count_upper_lower(s)
print("Uppercase:", u)
print("Lowercase:", l)
