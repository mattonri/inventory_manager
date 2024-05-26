import sqlite3
def drop_table(cur):
    try:
        cur.execute('DROP TABLE IF EXISTS product')
        cur.execute('DROP TABLE IF EXISTS discount_type')
        cur.execute('DROP TABLE IF EXISTS discount')
        print("Tables Dropped")

    except sqlite3.Error as e:
        print(f"An SQLite error occurred while dropping tables: {e}")


def generate_table(cur):
    try:

        # Create `product` table
        cur.execute('''
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            product_price REAL NOT NULL
        )
        ''')

        # Create `discount_type` table
        cur.execute('''
        CREATE TABLE IF NOT EXISTS discount_type (
            discount_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discount_type_name TEXT NOT NULL
        )
        ''')

        # Create `discount` table
        cur.execute('''
        CREATE TABLE IF NOT EXISTS discount (
            discount_code INTEGER PRIMARY KEY,
            discount_amount INTEGER,
            discount_type_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            FOREIGN KEY (discount_type_id) REFERENCES discount_type(discount_type_id),
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        )
        ''')

        # Create indexes for `discount` table
        cur.execute('''
        CREATE INDEX IF NOT EXISTS idx_discount_discount_type_id ON discount(discount_type_id)
        ''')
        cur.execute('''
        CREATE INDEX IF NOT EXISTS idx_discount_product_id ON discount(product_id)
        ''')


        # Insert a row of data
        print("Tables Generated")
        cur.execute('''INSERT INTO product (product_id, product_name, product_price) VALUES 
                (103071,'Catan: 5th Edition', 43.97),
                (104083,'Wooden Chess Set', 13.99),
                (105094,'Ticket to Ride', 49.99),
                (106105,'Pandemic', 39.99)''')
        cur.execute('''INSERT INTO discount (discount_code, discount_amount, discount_type_id, product_id) VALUES 
                (478,50,1,103071),
                (427,2,2,104083),
                (529,20,1,105094),
                (630,5,2,106105)''')
        cur.execute('''INSERT INTO discount_type (discount_type_id, discount_type_name) VALUES 
                (1,'Percent Off'),
                (2,'Dollars Off'),
                (3,'Free Shipping')''')

        # Save (commit) the changes
        print("Tables Populated")
    
    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the connection is closed even if an error occurs
        if 'cur' in locals():
            cur.close()