# not condition

shoe_price = float(input("Please enter price of shoe: "))

if shoe_price < 9.99:
	cheap_shoe = True 
else:
	cheap_shoe = False
	
if not cheap_shoe:
	print("The shoe is expensive")
else:
	print("This shoe is cheap")
