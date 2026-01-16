password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 != password2:
    print("Error: passwords do not match")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: password must be between 8 and 12 characters")
else:
    print("Password set")
