def money_predictor(total):
    coins = {"penny": 0.01, "nickel": 0.05, "dime": 0.10, "quarter": 0.25}
    bills = {"one": 1.00, "five": 5.00, "ten": 10.00, "twenty": 20.00}

    amount = 0.00
    while amount < total:
        user_input = input("Enter a coin or bill type: ")
        if user_input in coins:
            amount += coins[user_input]
        elif user_input in bills:
            amount += bills[user_input]
        else:
            print("Invalid input. Please try again.")
    
    return amount

total = float(input("Enter the total amount: "))
result = money_predictor(total)
print(f"The amount needed to add up to {total} is {result:.2f}")