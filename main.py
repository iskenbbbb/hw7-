import sqlite3


def create_connection(db_hw):
    connection = None
    try:
        connection = sqlite3.connect(db_hw)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    sql = '''INSERT INTO product 
    (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)




def update_quantity(conn, product):
    sql = '''UPDATE product SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)



def update_price(conn, product):
    sql = '''UPDATE product SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_student(conn, id):
    sql = '''DELETE FROM product WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products_and_print(conn):
    sql = '''SELECT * FROM product'''
    print(sql)

    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_product(conn):
    sql = '''SELECT * from product
    WHERE price <= 100 and quantity <= 5'''
    print('-------')
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
    return rows_list
def select_prod_search(conn, search):
    sql = '''SELECT * from product
    WHERE product_title like ?'''
    print(sql)
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + search + '%',))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

    #
    # print(sql)
    # try:
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #
    #     rows_list = cursor.fetchall()
    #     for row in rows_list:
    #         print(row)
    # except sqlite3.Error as e:
    #     print(e)


sql_create_table_product = '''
create table product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''


connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    create_table(connection_to_db, sql_create_table_product)

    # insert_product(connection_to_db, ('чай', 50, 24))
    # insert_product(connection_to_db, ('кофе', 115, 60))
    # insert_product(connection_to_db, ('хлеб', 30, 20))
    # insert_product(connection_to_db, ('батон', 50, 23))
    # insert_product(connection_to_db, ('печенье', 39, 99))
    # insert_product(connection_to_db, ('гоколад', 214, 89))
    # insert_product(connection_to_db, ('конфеты', 300, 40))
    # insert_product(connection_to_db, ('яйца', 15, 255))
    # insert_product(connection_to_db, ('молоко', 70, 36))
    # insert_product(connection_to_db, ('члебцы', 102, 103))
    # insert_product(connection_to_db, ('рис', 60, 80))
    # insert_product(connection_to_db, ('сахар', 100, 73))
    # insert_product(connection_to_db, ('мука', 90, 55))
    # insert_product(connection_to_db, ('макароны', 124, 158))
    # insert_product(connection_to_db, ('кетчуп', 395, 100))
    # insert_product(connection_to_db, ('майонез', 100, 488))
# ree = select_all_products_and_print(connection_to_db)

# add = update_price(connection_to_db, (200, 4))

# delete = delete_student(connection_to_db, 3)

# select_all_print = select_all_products_and_print(connection_to_db)
# sdvms = select_product(connection_to_db)
# print(sdvms)
vdjnd = select_prod_search(connection_to_db, 'х')

