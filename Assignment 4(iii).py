print("Welcome To Movie Theater")
persons = int(input("Enter the no. of Person : "))

total_price = 0

for i in range(1, persons + 1):
    age = int(input("Enter The Age Of Person: "))
    if age <= 3:
        print("Your Ticket is Free! Enjoy Your Movie")
    elif age <= 12:
        print("Your Ticket price will be $10")
        total_price += 10
    else:
        print("Your Ticket price will be $15")
        total_price += 15

print("Total Amount = ", total_price, " $ Enjoy Your Movie")
