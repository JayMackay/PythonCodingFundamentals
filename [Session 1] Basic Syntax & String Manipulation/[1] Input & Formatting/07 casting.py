# Casting is converting data from one type to another

product_name = input("What is the product name?")
product_price = float(input("What is the price?")) # cast string to float
product_quantity = int(input("How many products are there?")) # cast string to integer

product_price_str = input("What is the new price?")
product_price = float(product_price_str)

total_price = product_quantity * product_price

print(f"Total price: {total_price}")
