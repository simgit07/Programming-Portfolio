# Beckett Pizza Plaza - 4 for 3 Pizza Offer
# Program to calculate the total price and discount

print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

prices = []   # List to store the four pizza prices


# Loop to input four valid prices
for i in range(1, 5):
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{i}: "))

            # Check for valid price
            if price <= 0:
                print("Please enter a valid price!")
            else:
                prices.append(price)
                break   # exit loop when valid price is entered

        except:
            print("Please enter a valid price!")


# Calculate the total price before discount
total_price = sum(prices)

# Find the cheapest pizza (free one)
cheapest_price = min(prices)

# Apply the 4-for-3 discount
final_total = total_price - cheapest_price

# Calculate the discount percentage
discount_percentage = (cheapest_price / total_price) * 100

# Display the result
print(f"\nOrder Total is £{final_total:.2f}, a fabulous discount of {discount_percentage:.0f}%!")
