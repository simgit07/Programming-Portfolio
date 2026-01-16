import random
import string

def encrypt(message):
    interval = random.randint(2, 20)
    encrypted = []
    
    for char in message.replace(" ", ""):
        encrypted.append(char)
        for _ in range(interval - 1):
            encrypted.append(random.choice(string.ascii_lowercase))

    return "".join(encrypted), interval


msg = input("Enter a message: ")
encrypted_msg, step = encrypt(msg)
print("Encrypted message:", encrypted_msg)
print("Interval used:", step)
