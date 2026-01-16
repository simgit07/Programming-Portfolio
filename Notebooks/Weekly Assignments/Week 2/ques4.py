sweets = int(input("Enter the number of sweets: "))
pupils = int(input("Enter the number of pupils: "))

each = sweets // pupils
left = sweets % pupils

print("Each pupil will get", each, "sweets.")
print("There will be", left, "sweets left over.")
