products=[]
def add_new_product(newproduct,price,quantity):
    if newproduct.strip() == "":
        print("Invalid product name")
        return False

    for product in products:
        if newproduct.lower() == product["name"].lower():
            print("Product already exists")
            return False

    if price < 0:
        print("Price cannot be negative")
        return False

    if quantity < 0:
        print("Quantity cannot be negative")
        return False

    new_product = {
        "name": newproduct,
        "price": price,
        "quantity": quantity
    }

    products.append(new_product)
    print("Product added successfully")
    return True

def search_for_product(searched_product):
    for product in products:
        if searched_product.lower() == product["name"].lower():
            return product
    return (f"{searched_product} is not found in products")
def update_product_price(uproduct,newprice):
    if newprice < 0:
        print("Price cannot be negative")
        return False

    for product in products:
        if uproduct.lower() == product["name"].lower():
            product["price"] = newprice
            print("Price updated successfully")
            return True

    print("Product not found")
    return False
def increase_stock(uproduct,newquantity):
    if newquantity < 0:
        print("Quantity cannot be negative")
        return False

    for product in products:
        if uproduct.lower() == product["name"].lower():
            product["quantity"] += newquantity
            print("Stock increased successfully")
            return True

    print("Product not found")
    return False

def sell_a_product(sproduct,salequantity):
     if salequantity <= 0:
        print("Sale quantity must be greater than zero")
        return False

     for product in products:
        if sproduct.lower() == product["name"].lower():
            if salequantity <= product["quantity"]:
                product["quantity"] -= salequantity
                print("Product sold successfully")
                return True
            else:
                print("Not enough stock available")
                return False
     print("Product not found")
     return False
def calculate_the_total_inventory_value(products):
    inventory_value=0
    for product in products:
        inventory_value +=product["price"] * product["quantity"]
    return inventory_value
def generate_a_low_stock_report(product_list, minimum_stock=5):
    low_stock_products = []

    for product in product_list:
        if product["quantity"] < minimum_stock:
            low_stock_products.append(product)

    return low_stock_products

while True:
    print("\n===== INVENTORY STOCK CONTROLLER =====")
    print("1. Add a new product")
    print("2. Search for a product")
    print("3. Update product price")
    print("4. Increase stock")
    print("5. Sell a product")
    print("6. Calculate total inventory value")
    print("7. Generate low-stock report")
    print("8. Display all products")
    print("9. Exit")

    choice = input("Enter your choice: ")
    print("DEBUG:", repr(choice))

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter stock quantity: "))
        add_new_product(name, price, quantity)

    elif choice == "2":
        name = input("Enter product name to search: ")
        print(search_for_product(name))

    elif choice == "3":
        name = input("Enter product name: ")
        price = float(input("Enter new price: "))
        update_product_price(name, price)

    elif choice == "4":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))
        increase_stock(name, quantity)

    elif choice == "5":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to sell: "))
        sell_a_product(name, quantity)

    elif choice == "6":
        total = calculate_the_total_inventory_value(products)
        print(f"Total inventory value: {total:.2f} Birr")

    elif choice == "7":
        threshold = int(input("Enter low-stock threshold (default is 5): "))
        low_stock = generate_a_low_stock_report(products, threshold)

        if low_stock:
            print("\n--- LOW-STOCK REPORT ---")
            for product in low_stock:
                print(
                    f"Name: {product['name']}, "
                    f"Quantity: {product['quantity']}"
                )
        else:
            print("No low-stock products found")

    elif choice == "8":
       print("Option 8 selected!")
       print("Products list:", products)

       if products:
         for product in products:
            print(product)
       else:
         print("No products in inventory")
    elif choice == "9":
        print("Thank you for using the inventory system!")
        break

    else:
        print("Invalid choice. Please try again.")
