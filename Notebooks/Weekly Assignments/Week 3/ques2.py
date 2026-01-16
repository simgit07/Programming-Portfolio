password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 == password2:
    print("Password set")
else:
    print("Error: passwords do not match")
