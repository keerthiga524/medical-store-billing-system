
medicines = {}

def add_medicine():
    name = input("Enter medicine name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    medicines[name] = {"price": price, "qty": qty}
    print("Medicine added successfully!\n")

def view_medicines():
    if not medicines:
        print("No medicines available.\n")
    else:
        print("\nAvailable Medicines:")
        for name, details in medicines.items():
            print(f"{name} - Price: {details['price']} | Qty: {details['qty']}")
        print()

def sell_medicine():
    name = input("Enter medicine name to sell: ")
    if name in medicines:
        qty = int(input("Enter quantity to sell: "))
        if qty <= medicines[name]["qty"]:
            total = qty * medicines[name]["price"]
            medicines[name]["qty"] -= qty
            print("\n----- BILL -----")
            print("Medicine:", name)
            print("Quantity:", qty)
            print("Total Amount: Rs.", total)
            print("----------------\n")
        else:
            print("Not enough stock!\n")
    else:
        print("Medicine not found!\n")

while True:
    print("==== Medical Store Billing System ====")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Sell Medicine")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_medicine()
    elif choice == "2":
        view_medicines()
    elif choice == "3":
        sell_medicine()
    elif choice == "4":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, try again.\n")
