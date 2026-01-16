
menu = {
    'Pizza': 40,
    'Pasta': 30,
    'Salad': 20,
    'Burger': 50,
    'Coffee': 15,
    'Tea': 10,

}

print ("Welcome to PYTHON Restaurant!")
print("Pizza: Rs40\nPasta: Rs30\nSalad: Rs20\nBurger: Rs50\nCoffee: Rs15\nTea: Rs10")

order_total = 0
item_1 = input("Enter the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Enter the  name of second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")  

print(f"Your total order amount of items to pay is: Rs{order_total}")    