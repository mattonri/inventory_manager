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
    print()
    view_products(cur)
    add_product(cur)
    view_products(cur)

    # menu(cur, con)
    con.close()


def menu(cur, con):
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

    print("Thank you. Goodbye.")

class product:
    def __init__(self, id_number, cur):
        self.id_number = id_number
        cur.execute(f'''
            SELECT * 
            FROM product 
            LEFT JOIN discount ON product.product_id = discount.product_id
            LEFT JOIN discount_type ON discount.discount_type_id = discount_type.discount_type_id
            WHERE product.product_id LIKE '{id_number}'
        ''')
        data = cur.fetchall()
        # print(data)
        # Take it out of the list
        data = data[0]
        self.name = data[1]
        self.price = data[2]
        if len(data) > 3:
            self.discount_code = data[3]
            self.discount_type = data[8]
            self.discount_amount = data[4]
            self.discount_type_code = data[5]

    # # For this project I implemented this a different way, but in the future I might add a new way to create the product object and use this to add it to the database
    # def register_product(self, cur):
    #     cur.execute(f'''INSERT INTO product (product_id, product_name, product_price) VALUES 
    #             ({self.id_number},'{self.name}', {self.price})''')
    #     if not self.discount_code == "":
    #         cur.execute(f'''INSERT INTO discount (discount_code, discount_amount, discount_type_id, product_id) VALUES 
    #                 ({self.discount_code},{self.discount_amount},{self.discount_type_code},{self.id_number})''')
    #         if not self.discount_type_code == "":
    #             cur.execute(f'''INSERT INTO discount_type (discount_type_id, discount_type_name) VALUES 
    #                     ({self.discount_type_code},'{self.discount_type}')''')
    
    def __str__(self):
        return f"ID:{self.id_number} \tName:{self.name} \tPrice:{self.price} \tDiscount Code:{self.discount_code} \tDiscount Type:{self.discount_type} \tDiscount Amount:{self.discount_amount}"
    

def add_product(cur):
    product_id = input("What is the ID of the product that you would like to add? (Usually a 6 digit number)")
    product_name = input("What is the name of the product that you would like to add?")
    product_price = input("What is the price of the product that you would like to add?")
    cur.execute(f'''INSERT INTO product (product_id, product_name, product_price) VALUES 
        ({product_id},'{product_name}', {product_price})''')


def view_products(cur):
    print(f"Currently Registered Products:")
    cur.execute(f'''
        SELECT product_id 
        FROM product 
    ''')
    product_id_rows = cur.fetchall()
    for product_id in product_id_rows:
        iterate_product = product(product_id[0], cur)
        print(iterate_product)
    



def remove_products(cur):
    print("Here are all of the current products:")
    view_products(cur)
    try:
        remove_id = input("What is the product ID of the item you would like to remove?")
        cur.execute(f'''
            DELETE FROM product
            WHERE product_id = {remove_id}
        ''')
    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
    

if __name__ == "__main__":
     main()