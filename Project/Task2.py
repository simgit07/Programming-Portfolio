import random

# Ask the user to enter a password
password = input("Enter your password: ")

# Check the length of the password
if len(password) < 9:
    print("\nPassword too short.")
else:
    # If the password is long enough, perform 3 security checks
    passed = True

    for i in range(3):
        # Generate a random position (1 to length of password)
        position = random.randint(1, len(password))

        # Ask the user for the letter at that position
        user_letter = input(f"\nEnter letter at position {position}: ")

        # Check if the entered letter is correct
        if user_letter == password[position - 1]:
            print("\nCorrect")
        else:
            print("\nSecurity check failed.")
            passed = False
            break   # Exit immediately if any check is wrong

    # If all checks were correct
    if passed:
        print("\nSecurity check passed.")
