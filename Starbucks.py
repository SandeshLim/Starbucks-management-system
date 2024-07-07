class Starbucks:
    def __init__(self):
        self.menu = {
            "Espresso": 2.90,
            "Latte": 3.60,
            "Cappuccino": 3.60,
            "Americano": 3.40,
            "Mocha": 3.45,
        }

        self.inventory = {
            "Espresso": 10,
            "Latte": 10,
            "Cappuccino": 10,
            "Americano": 10,
            "Mocha": 10,
        }

        self.sales = 0.0

    def display_menu(self):
        print("\n-- Menu --")
        for item, price in self.menu.items():
            print(f"{item}: £{price:.2f}")
        print("-------------------------------\n")

    def take_order(self):
        self.display_menu()
        order = input("What would you like to order? \n\n").capitalize()
        if order in self.menu:
            if self.inventory[order] > 0:
                try:
                    quantity = int(input("How many would you like to order? \n\n"))
                    if quantity <= self.inventory[order]:
                        self.process_order(order, quantity)
                    else:
                        print(f"Sorry, we don't have enough {order}.")
                except ValueError:
                    print("Please enter a valid quantity.")
            else:
                print(f"Sorry, we're out of {order}.")
        else:
            print("Sorry, we don't have that item on the menu.")

    def process_order(self, order, quantity):
        cost = self.menu[order] * quantity
        print(f"Your order: {quantity} {order}(s) for £{cost:.2f}")
        confirm = input("Would you like to proceed with the order? \n\n (yes/no) \n\n").lower()
        if confirm == "yes":
            self.sales += cost
            self.inventory[order] -= quantity
            print(f"Thank you! Your order for {quantity} {order}(s) has been placed.")
        else:
            print("Order canceled.")

    def display_sales(self):
        print(f"\nTotal sales: £{self.sales:.2f}")

    def display_inventory(self):
        print("\n--- Inventory ---")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print("-------------------------------\n")


def main():
    shop = Starbucks()
    while True:
        print("\nWelcome to the Starbucks coffee management system")
        print("1. Place an order")
        print("2. View sales")
        print("3. View inventory")
        print("4. Exit")

        choice = input("Please select an option: ")
        if choice == "1":
            shop.take_order()
        elif choice == "2":
            shop.display_sales()
        elif choice == "3":
            shop.display_inventory()
        elif choice == "4":
            print("Thank you for using the Starbucks coffee management system. See you next time!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()







    
  