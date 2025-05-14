import pandas as pd
from products import name_to_id, get_products, update_products, delete_product, add_product
from inventory import change_stock
from balance import check_balance, update_balance

def display_main_menu():
    while True:
        options = ["1", "2", "3", "0"]
        choice = input(
            "Welcome to STOCK MANAGEMENT!!\n"
            "Choose an option:\n"
            "1: Inventory\n"
            "2: Balance\n"
            "3: Products\n"
            "0: Exit\n"
            ">> "
        )
        if choice in options:
            return choice
        print("Invalid input. Please choose from the available options.")

def inventory_menu():
    while True:
        choice = input(
            "\nINVENTORY MENU:\n"
            "1: Look for Product by Name\n"
            "2: Change Stock\n"
            "3: View All Products\n"
            "0: Exit\n"
            ">> "
        )
        if choice == '0':
            break
        elif choice == '1':
            product_name = input("Enter product name to get its ID: ")
            print(name_to_id(product_name))
        elif choice == '2':
            try:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity to Add/Subtract: "))
                change_stock(product_id, quantity)
                print("Stock updated successfully.")
            except ValueError:
                print("Invalid input. Please enter integers for ID and Quantity.")
        elif choice == '3':
            products = get_products()
            print(pd.DataFrame(products, columns=["index", "p_id", "buy_p", "sell_p"]))
        else:
            print("Invalid option. Please choose again.")

def balance_menu():
    while True:
        choice = input(
            "\nBALANCE MENU:\n"
            "1: Check Balance\n"
            "2: Update Balance\n"
            "0: Exit\n"
            ">> "
        )
        if choice == '0':
            break
        elif choice == '1':
            data = check_balance()
            df = pd.DataFrame([data], columns=["Balance", "Money in Stock", "ID"])
            print(df)
        elif choice == '2':
            try:
                amount = int(input("Enter amount (+ to add, - to subtract): "))
                update_balance(amount)
                print("Balance updated.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid option. Please choose again.")

def products_menu():
    while True:
        choice = input(
            "\nPRODUCTS MENU:\n"
            "1: Add Product\n"
            "2: Delete Product\n"
            "3: Update Product\n"
            "0: Exit\n"
            ">> "
        )
        if choice == '0':
            break
        if choice == "1":
            try:
                product_input = input("Enter values as: product_name,buying_price,selling_price\n>> ")
                name, buying, selling = [x.strip() for x in product_input.split(",")]
                buying = float(buying)
                selling = float(selling)
                add_product(name, buying, selling)
                print("Product added.")
            except Exception as e:
                print(f"Error adding product: {e}")
        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID to delete: "))
                delete_product(product_id)
                print("Product deleted.")
            except Exception as e:
                print(f"Error deleting product: {e}")
        elif choice == "3":
            try:
                update_input = input("Enter values as: product_id,product_name,buying_price,selling_price\n>> ")
                prod_id, prod_name, buying, selling = [x.strip() for x in update_input.split(",")]
                prod_id = int(prod_id)
                buying = float(buying)
                selling = float(selling)
                update_products(prod_name, selling, buying, prod_id)
                print("Product updated.")
            except Exception as e:
                print(f"Error updating product: {e}")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    while True:
        menu_choice = display_main_menu()

        if menu_choice == "1":
            inventory_menu()
        elif menu_choice == "2":
            balance_menu()
        elif menu_choice == "3":
            products_menu()
        elif menu_choice == "0":
            print("Exiting program. Goodbye!")
            break
            


        
        


