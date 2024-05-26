# Overview

This program is a product manager for board games. It uses an SQL relational database to handle products with a variety of different discounts applied to them. It functions fully in the command line and it has a few functions in product_manager to generate the database in case the file is lost or if you need to delete it, it will set it back the way that it was. I wrote it to learn sqlite better and brush up on python classes. 

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

My diagram has 3 tables. One to store the products, another to store specific discounts for specific products and one last one to store the text of the discount type (According to database best practices)
![mysql database diagram](./Screenshot%202024-05-24%20183357.png)
{Describe the structure (tables) of the relational database that you created.}

# Development Environment

I made a diagram of the database in mysql worbench since I had experience in it but the program itself is just made of python with the sqlite module.
# Useful Websites

- [Official SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Wr3 SQLite Tutorial](https://www.w3resource.com/sqlite/)

# Future Work

I would add more manipulation to discounts and maybe even more tables to keep track of inventory (as the program originally intended), orders and more.
- Add and delete discounts
- Add inventory tables
- Add order and customer info tables