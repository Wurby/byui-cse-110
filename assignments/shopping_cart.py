# #Have menu system that repeats until the user chooses quit.
# Create a list that will store the names of the items in the shopping cart.
# Complete the option to add the name of the item to the list.
# Complete the option to display the names of the items in the list.
# Store prices as well as names.
# Change the add functionality to also ask for and store the price of the item.
# Change the display functionality to also display the prices of the items.
# When displaying the items, display a number in front of each item. The numbers should start with 1.
# Complete the option to display the total amount of the prices of all the items in the shopping cart.
# Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol(for example $, €, etc.)
# Complete the option to remove an item from the shopping cart.
# When removing an item, you should verify the following:
# Both the item name and price are removed from their respective lists.
# The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
# The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

class Menu():
    def __init__(self):
        self.cart = Cart()
        self.choices = [
            "Add item",
            "View cart",
            "Remove item",
            "Compute total",
            "Quit"
        ]
        self.selection = "Not quit"
        self.run()

    def run(self):
        while self.selection != "Quit":
            self.give_menu()
            self.take_choice()
            self.process()

    def give_menu(self):
        print("Please select one of the following.")
        for index, menu_item in enumerate(self.choices):
            print(f'{index + 1}. {menu_item}')

    def quit(self):
        print("Thank you, good-bye.")
        self.selection = "Quit"

    def take_choice(self):
        self.selection = input("Please enter an action: ")

    def process(self):
        if self.selection == "1":
            self.cart.add_to_cart()
        elif self.selection == "2":
            self.cart.display_cart()
        elif self.selection == "3":
            self.cart.remove_item()
        elif self.selection == "4":
            self.cart.calculate_total()
        elif self.selection == "5":
            self.quit()
        else:
            print("Incorrect option, try again.")


class Cart():
    def __init__(self):
        self.items = []

    def add_to_cart(self):
        item = input("What would you like to add? ").title()
        price = None
        while type(price) != float:
            try:
                price = float(input(f"What is the price of '{item}'? "))
            except ValueError:
                print(f"That is not a valid price!")
        self.items.append((item, price))
        print(f"'{item}' has been added to the cart.")
        print()

    def remove_item(self):
        item_number = int(input("Which item would you like to remove? "))
        self.items.pop(item_number - 1)
        print("Item removed.")
        print()

    def calculate_total(self):
        total = 0.00
        for (item, price) in self.items:
            total += price
        print(
            f"The total price of the items in the shopping cart is ${total:.2f}")
        print()

    def display_cart(self):
        for index, (item, price) in enumerate(self.items):
            print(f"{index + 1}. {item:<8}- ${price:>6.2f}")
        print()


Menu()
