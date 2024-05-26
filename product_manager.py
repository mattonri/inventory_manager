import sqlite3
from table_generator import generate_table, drop_table


def main():
    con = sqlite3.connect('product.db')
    cur = con.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='product';")
    exists_product = cur.fetchone()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='discount';")
    exists_discount = cur.fetchone()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='discount_type';")
    exists_discount_type = cur.fetchone()
    if not (exists_product and exists_discount and exists_discount_type):
        print("The product database doesn't have all the necessary files and will be re-generated!")
        with open('filename.txt', 'w') as file:
            pass
        drop_table(cur)
        generate_table(cur)
        con.commit()
    
    catan = item(103071, cur)
    # menu(cur, con)
    con.close()


def menu(cur, con):
    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    con.commit()

    action = 0
    shopping_cart = []
    print("Welcome to the Shopping Cart Program!")
    while action != 6:
        print('''\nPlease select one of the following: 
        1. Add Product
        2. View Product List
        3. Remove Products
        4. See Discounts
        5. Add Discounts
        6. Delete Discounts
        7. Quit''')
        action = int(input("Please enter an action: "))
        while not action in (1, 2, 3, 4, 5, 6, 7):
                print("sorry, that's not a valid input")
                action = int(input("Please enter an action: "))
        if action == 1:
            add_product(cur)
            con.commit()
        elif action == 2:
            view_products(cur)
            con.commit()
        elif action == 3:
            remove_products(cur)
            con.commit()
        elif action == 4:
            see_discounts(cur)
            con.commit()
        elif action == 5:
            add_discounts(cur)
            con.commit()
        elif action == 6:
            delete_discounts(cur)
            con.commit()

    print("Thank you. Goodbye.")

class item:
     def __init__(self, id_number, cur):
        self.id_number = id_number
        cur.execute(f'''
            SELECT * 
            FROM product 
            JOIN discount ON product.product_id = discount.product_id
            JOIN discount_type ON discount.discount_type_id = discount_type.discount_type_id
            WHERE product.product_id LIKE '{id_number}'
        ''')
        data = cur.fetchall()
        print(data)
        self.name = data[1]
        self.price = data[2]
        self.discount_code = data[3]
        self.discount_type = data[8]
        self.discount_amount = data[4]


def add_product(cur):
    new_item = input("What item would you like to add? ")
    new_price = float(input(f"What is the price of '{new_item}'? "))
    cur.append((new_price, new_item))
    print(f"'{new_item}' has been added to the cart.")


def view_products(cur):
    print(f"")
            cur.execute(f'''
            SELECT * 
            FROM product 
            JOIN discount ON product.product_id = discount.product_id
            JOIN discount_type ON discount.discount_type_id = discount_type.discount_type_id
            WHERE product.product_id LIKE '{id_number}'
        ''')
        data = cur.fetchall()
        print(data)
    



def remove_products(cur):
    remove_i = (int(input("Which item would you like to remove? ")) - 1)
    if remove_i >= 0 and remove_i <= len(cur):
        cur.pop(remove_i)
        print("Item removed.")
    else:
         print("Sorry, that is not a valid item number.")


def see_discounts(cur):
    total = 0
    for item in cur:
        total += item[0]
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

def add_discounts(cur):
    cur.sort()
    print("Cart sorted!")
    # view_cart(shopping_cart)

def delete_discounts(cur):
    pass

if __name__ == "__main__":
     main()