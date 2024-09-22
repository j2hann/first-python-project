discount = 0.10

firstItem = int(input("Enter the price of your first item: "))
secondItem = int(input("Enter the price of your second item: "))
thirdItem = int(input("Enter the price of your third item: "))

totalAmount = firstItem + secondItem + thirdItem
print("Total amount purchased: " + str(totalAmount))

if totalAmount > 100:
    discountAmount = totalAmount * discount
    newTotalAmount = totalAmount - discountAmount
    loyalty = newTotalAmount / 10
    loyalty = round(loyalty, 2)
    print("You are qualified for a discount. Your new total amount is " + str(newTotalAmount))
    print("Loyalty Points Earned: " + str(loyalty))

    payment = int(input("Enter your payment (in whole numbers): "))
    if payment < newTotalAmount:
         print("You don't have enough money.")
    else:
         change = payment - newTotalAmount
         change = round(change, 2)
         print("Your change is " + str(change))
        
else:
    loyalty = totalAmount / 10
    loyalty = round(loyalty, 2)
    print("You are not qualified for a discount")
    print("Loyalty Points Earned: " + str(loyalty))
    
    payment = int(input("Enter your payment (in whole numbers): "))
    if payment < totalAmount:
         print("You don't have enough money.")
    else:
        change = payment - totalAmount
        change = round(change, 2)
        print("Your change is " + str(change))
