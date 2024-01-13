#Functions
def calculate_discount(original_price, discount_percentage=10):

    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

original_price = 100.0
discounted_price = calculate_discount(original_price)

print(f"Original Price: ${original_price}")
print(f"Discounted Price (10% off): ${discounted_price}")
