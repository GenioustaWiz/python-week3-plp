def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price
    return final_price
print("=============================================================")
print("=============================================================")
print("This is a Simple Calculator. It checks if the discount percentage of an Item is 20% or higher. If it is, it calculates the final price by subtracting the discount amount from the original price")
print("=============================================================")
print("=============================================================")
item_name = input('Please enter name of Item: ')

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print(f"The final price of {item_name} after applying the discount is: {final_price}" )
