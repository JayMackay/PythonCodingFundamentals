# if-elif statement

print("1 - All Running Trainers")
print("2 - All Classic Trainers")
print("3 - All Boots and Shoes")

menuOption = int(input("Select an option 1, 2 or 3: "))

if menuOption == 1:
	print("These are all the Running Trainers")
elif menuOption == 2:
	print("These are all the Classics")
elif menuOption == 3:
	print("This are all the Boots and Shoes")
else:
	print("You didn’t choose the correct option")
