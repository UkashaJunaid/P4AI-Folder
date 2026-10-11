menu = {
    1: {"name": "Burger", "price": 500},
    2: {"name": "Pizza", "price": 800},
    3: {"name": "Fries", "price": 250},
    4: {"name": "Drink", "price": 150}
}


def calculate_bill(order):
    total = 0
    for item in order:
        total += item["price"] * item["quantity"]
    return total


order = []

while True:
    print("\nRESTAURANT MENU")
    for number, item in menu.items():
        print(number, ".", item["name"], "- Rs.", item["price"])
    print("0. Finish order")

    choice = input("Select an item number: ")

    if choice == "0":
        break

    if not choice.isdigit() or int(choice) not in menu:
        print("Invalid choice. Please select an item from the menu.")
        continue

    choice = int(choice)
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    selected_item = menu[choice]
    order.append({
        "name": selected_item["name"],
        "price": selected_item["price"],
        "quantity": quantity
    })
    print("Item added to order.")

total = calculate_bill(order)

print("\nRESTAURANT BILL")
if not order:
    print("No items ordered.")
else:
    for item in order:
        item_total = item["price"] * item["quantity"]
        print(item["name"], "-", item["quantity"], "x Rs.", item["price"],
              "= Rs.", item_total)
print("Final bill: Rs.", total)

with open("orders.txt", "w", encoding="utf-8") as file:
    file.write("RESTAURANT BILL\n")
    if not order:
        file.write("No items ordered.\n")
    else:
        for item in order:
            item_total = item["price"] * item["quantity"]
            file.write(item["name"] + " - " + str(item["quantity"]) +
                       " x Rs. " + str(item["price"]) +
                       " = Rs. " + str(item_total) + "\n")
    file.write("Final bill: Rs. " + str(total) + "\n")

print("Bill saved in orders.txt")
