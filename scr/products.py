import psycopg2
from database import get_connection

def name_to_id(product_name):
    conn = None
    cur =None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """SELECT id FROM product WHERE product_name = %s""", (product_name,)
            )
            product_id = cur.fetchone()
            if product_id:
                return product_id[0]
            else:
                return f'No product found with name {product_name}'
    except Exception as e:
        print(f"Something went wrong in updating \n{e}")

    finally:
        if conn:
            conn.close()
        if cur:
            cur.close()

def add_product(product_name:str, purchase_price:int, selling_price:int):
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO product (product_name, selling_price, purchase_price)
                VALUES (%s,%s,%s) RETURNING id""", (product_name, purchase_price, selling_price)
            )
            product_id = cur.fetchone()[0]
            conn.commit()
            print(f'PRODUCT {product_name} with ID {product_id}')
    except psycopg2.errors.UniqueViolation:
        print(f"Product name exist {product_name}")
    except Exception as e:
        print(f'Something went wrong❌\n {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def delete_product(id):
    cur = None
    conn = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """DELETE FROM product WHERE id=%s""", (id,)
            )
            if cur.rowcount > 0:
                print(f'Product with ID {id} is deleted')
            else:
                print(f'No product found at id {id}')
            conn.commit()
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        
def update_products(product_name, selling_price, purchase_price, id):
    cur = None
    conn = None
    try:    
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """UPDATE product SET product_name = %s, selling_price = %s, purchase_price= %s WHERE id = %s""",
                (product_name, selling_price, purchase_price, id)
            )
            conn.commit()
    except Exception as e:
        print(f'Something went wrong in updating products {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    

def get_products():
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM product')
            products = cur.fetchall()
            products =  [list(product) for product in products]

            return products
    except Exception as e:
        print(f'something went wrong {e}')
        return []
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

