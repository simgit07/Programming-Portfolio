capitals = {}

while True:
    country = input("Enter a country (or 'quit' to stop): ").strip()
    if country.lower() == "quit":
        break

    key = country.lower()

    if key in capitals:
        print(f"The capital of {country} is {capitals[key]}.")
    else:
        capital = input(f"I don't know the capital of {country}. Enter it: ").strip()
        capitals[key] = capital
        print("Capital stored.")
