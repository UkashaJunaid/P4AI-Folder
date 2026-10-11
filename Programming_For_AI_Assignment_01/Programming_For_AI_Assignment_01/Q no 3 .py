products = []


def calculate_bill(product_list):
    total_bill = 0

    for product in product_list:
        product_total = product["price"] * product["quantity"]
        product["total"] = product_total
        total_bill += product_total

    discount = 0
    if total_bill > 10000:
        discount = total_bill * 0.10

    final_bill = total_bill - discount
    return total_bill, discount, final_bill


for i in range(5):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price in Rs.: "))
    quantity = int(input("Enter quantity: "))

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

total_bill, discount, final_bill = calculate_bill(products)
most_expensive = max(products, key=lambda item: item["price"])

print("\nSHOPPING BILL")
for product in products:
    print(product["name"], "-", product["quantity"], "x Rs.", product["price"],
          "= Rs.", round(product["total"], 2))

print("Total bill: Rs.", round(total_bill, 2))
print("Discount: Rs.", round(discount, 2))
print("Final bill: Rs.", round(final_bill, 2))
print("Most expensive product:", most_expensive["name"],
      "(Rs.", round(most_expensive["price"], 2), "each)")

with open("bill.txt", "w", encoding="utf-8") as file:
    file.write("SHOPPING BILL\n")
    for product in products:
        file.write(product["name"] + " - " + str(product["quantity"]) +
                   " x Rs. " + str(product["price"]) +
                   " = Rs. " + str(round(product["total"], 2)) + "\n")
    file.write("\nTotal bill: Rs. " + str(round(total_bill, 2)) + "\n")
    file.write("Discount: Rs. " + str(round(discount, 2)) + "\n")
    file.write("Final bill: Rs. " + str(round(final_bill, 2)) + "\n")
    file.write("Most expensive product: " + most_expensive["name"] + "\n")

print("\nBill saved in bill.txt")
