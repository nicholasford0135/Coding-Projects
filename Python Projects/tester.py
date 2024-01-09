# get the purchase amount and payment amount from the user
purchase_amount = float(input("Enter the purchase amount: "))
payment_amount = float(input("Enter the payment amount: "))

# calculate the change
change = payment_amount - purchase_amount

# print the change
print("The change is:", change)

# calculate the number of each type of coin/bill to give as change
dollars = int(change)
change -= dollars
quarters = int(change / 0.25)
change -= quarters * 0.25
dimes = int(change / 0.1)
change -= dimes * 0.1
nickels = int(change / 0.05)
change -= nickels * 0.05
pennies = round(change / 0.01)

# print the number of each type of coin/bill to give as change
print("Give the customer:")
print(dollars, "dollars")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")
