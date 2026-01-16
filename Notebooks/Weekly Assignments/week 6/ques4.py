def encrypt(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]


text = input("Enter a message: ")
print("Encrypted:", encrypt(text))
