import sqlite3

def main():
    action = 0
    shopping_cart = []
    print("Welcome to the Shopping Cart Program!")
    while action != 6:
        print('''\nPlease select one of the following: 
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Sort cart
        6. Quit''')
        action = int(input("Please enter an action: "))
        while not action in (1, 2, 3, 4, 5, 6):
                print("sorry, that's not a valid input")
                action = int(input("Please enter an action: "))
        if action == 1:
            add_item(shopping_cart)
        elif action == 2:
            view_cart(shopping_cart)
        elif action == 3:
            remove_item(shopping_cart)
        elif action == 4:
            compute_total(shopping_cart)
        elif action == 5:
            sort_cart(shopping_cart)

    print("Thank you. Goodbye.")

class item:
     def __init__(self, id_number, name, price):
          self.id_number = id_number
          self.name = name
          self.price = price


def add_item(shopping_cart):
    new_item = input("What item would you like to add? ")
    new_price = float(input(f"What is the price of '{new_item}'? "))
    shopping_cart.append((new_price, new_item))
    print(f"'{new_item}' has been added to the cart.")


def view_cart(shopping_cart):
    print(f"The contents of the shopping cart are: ")
    for i in range(len(shopping_cart)):
         print(f"{i + 1}. {shopping_cart[i][1]} - ${shopping_cart[i][0]:.2f}")


def remove_item(shopping_cart):
    remove_i = (int(input("Which item would you like to remove? ")) - 1)
    if remove_i >= 0 and remove_i <= len(shopping_cart):
        shopping_cart.pop(remove_i)
        print("Item removed.")
    else:
         print("Sorry, that is not a valid item number.")


def compute_total(shopping_cart):
    total = 0
    for item in shopping_cart:
        total += item[0]
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

def sort_cart(shopping_cart):
    shopping_cart.sort()
    print("Cart sorted!")
    # view_cart(shopping_cart)

print("Welcome to the Shopping Cart Program!")

while action != 6:
    print('''\nPlease select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Sort cart
    6. Quit''')
    action = int(input("Please enter an action: "))
    while not action in (1, 2, 3, 4, 5, 6):
            print("sorry, that's not a valid input")
            action = int(input("Please enter an action: "))
    if action == 1:
        add_item(shopping_cart)
    elif action == 2:
         view_cart(shopping_cart)
    elif action == 3:
         remove_item(shopping_cart)
    elif action == 4:
         compute_total(shopping_cart)
    elif action == 5:
         sort_cart(shopping_cart)

print("Thank you. Goodbye.")

if __name__ == "main":
     main()