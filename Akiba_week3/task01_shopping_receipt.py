
def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    return amount * tax_rate


def generate_receipt(items, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate!")
        return

    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            print("Price and quantity cannot be negative!")
            return

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)
    final_amount = amount_after_discount + tax

    print("\n===== SHOPPING RECEIPT =====")
    for item in items:
        print(f'{item["name"]} x {item["quantity"]} = '
              f'{item["price"] * item["quantity"]} Birr')

    print("----------------------------")
    print(f"Subtotal: {subtotal:.2f} Birr")
    print(f"Discount: {discount:.2f} Birr")
    print(f"Tax: {tax:.2f} Birr")
    print(f"Final Amount: {final_amount:.2f} Birr")
    print("============================")


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

tax_rate = 0.15

generate_receipt(items, tax_rate)
