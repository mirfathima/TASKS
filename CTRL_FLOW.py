#Control Flow
mixed_data = ["apple", 100, True, 3.14, "banana", None]

discounted_price = 75

if discounted_price < 50:
    print("Low-cost item.")
elif discounted_price >= 50 and discounted_price < 100:
    print("Moderate-cost item.")
else:
    print("High-cost item.")

for element in mixed_data:
    if element is None:
        break
    print(f"Element: {element}, Data type: {type(element)}")


