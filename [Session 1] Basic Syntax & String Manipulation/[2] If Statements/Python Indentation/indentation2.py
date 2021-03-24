age = 10

if age < 2:
    print("Infant fare.")
    print("Cost is 10% of adult fare.")
elif 2 <= age <= 11:
  print("Child fare.")
  print("Cost is 50% of adult fare.")
elif 12 <= age <= 16:
      print("Young adult fare.")
      print("Cost is 75% of adult fare.")
else:
    print("Adult fare.")

# Do NOT do this though! It's difficult to read.
