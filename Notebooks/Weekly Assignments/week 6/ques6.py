def decrypt(encrypted, interval):
    message = []

    for i in range(0, len(encrypted), interval):
        message.append(encrypted[i])

    return "".join(message)


encrypted_msg = input("Enter encrypted message: ")
interval = int(input("Enter interval: "))
print("Decrypted message:", decrypt(encrypted_msg, interval))
