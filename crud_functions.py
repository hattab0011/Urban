import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,           
    )
    ''')

    connection.commit()
    connection.close()


def add_product():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
        ''', (title, description, price))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products

if __name__ == "__main__":
    initiate_db()
    add_product("Продукт 1", "Описание продукта 1", 100)
    add_product("Продукт 2", "Описание продукта 2", 200)
    add_product("Продукт 3", "Описание продукта 3", 300)
    add_product("Продукт 4", "Описание продукта 4", 400)