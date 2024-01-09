print("Welcome to the pool program")
choice = input("Would you like to calculate swims? (yes/no): ")
print("Please select which swim you would like to enter:")


if choice == "yes":
    print("Please enter the number of swims for each category")
    swim_A = int(input("How many Adults today: "))
    swim_B = int(input("How many Children today: "))
    swim_C = int(input("How many Seniors today: "))

    swim_r = int(input("How many Rentals today: "))

    total = swim_A + swim_B + swim_C

    print("There were", total, "people in the swim")

    print("There were", swim_A,  "Adults")
    print("There were", swim_B,  "Children")
    print("There were", swim_C, "Seniors")
    print("There were", swim_r,  "Rentals")

    print("Total for the swim is $",swim_A * 3.50 + swim_B * 2.50 + swim_C * 3.25, + swim_r * 80,"dollars")

else:
    print("Thank you for using the program")


    


