
from numpy import number


class Meals:
    def __init__(self):
        self.child = float(input("What is the price of child's meal? "))
        self.adult = float(input("What is the price of an adult's meal? "))


class Diners:
    def __init__(self):
        self.adult = int(input("How many adults are there? "))
        self.child = int(input("How many children are there? "))


def calculate_subtotal(meals, diners):
    subtotal = 0
    subtotal += meals.adult * diners.adult
    subtotal += meals.child * diners.child
    return subtotal


def calculate_tax(subtotal):
    tax_rate = float(input("What is the sales tax rate? "))
    return subtotal * tax_rate / 100


def accounting(subtotal, tax_amount):
    total = subtotal + tax_amount
    print("Subtotal: $" + f"{subtotal:.2f}".format(2))
    print("Sales Tax: $" + f"{tax_amount:.2f}".format(2))
    print("Total: $" + f"{total:.2f}".format(2))
    return total


def ask_payment(total):
    payment = float(input("What is the payment amount? "))
    while payment < total:
        print("Not enough payment")
        print()
        payment = float(input("What is the payment amount? "))
    if payment > 200:
        print("That's a lot of dough!")
    return payment


def change(total, payment):
    change = payment - total
    print("Change: $" + f"{change:.2f}".format(2))


meals = Meals()
diners = Diners()
print()
subtotal = calculate_subtotal(meals, diners)
tax_amount = calculate_tax(subtotal)
total = accounting(subtotal, tax_amount)
print()
payment = ask_payment(total)
change(total, payment)
