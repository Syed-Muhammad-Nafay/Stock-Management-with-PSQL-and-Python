import psycopg2
from database import get_connection
def change_stock(id, quantity):
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT selling_price, purchase_price FROM product WHERE id = %s", (id,))
            result = cur.fetchone()
            
            if result:
                selling_price = result[0]
                purchase_price = result[1]
                last_quantity = 0
                cur.execute("SELECT quantity FROM inventory WHERE product_id = %s", (id,))
                row = cur.fetchone()
                if row:
                    last_quantity = row[0]
        
                cur.execute(
                    """INSERT INTO inventory (product_id, quantity) 
                    VALUES (%s, %s)
                    ON CONFLICT (product_id) DO UPDATE 
                    SET quantity = EXCLUDED.quantity""",
                    (id, quantity),
                )
                remaining_quantity = quantity - last_quantity
                mode = "Purchase" if remaining_quantity > 0 else "Sale" if remaining_quantity < 0 else "None"
                total_value_when_selling = abs(remaining_quantity) * selling_price
                total_value_when_buying = abs(remaining_quantity) * purchase_price
                print(f"{quantity} updated to stock at ID {id}: Transaction of {remaining_quantity}")
                if mode == 'Purchase':
                    cur.execute(
                        """INSERT INTO transactions (product_id, quantity, total_price, mode, transaction_date)
                        VALUES (%s, %s, %s, %s, NOW())""", (id, abs(remaining_quantity), total_value_when_buying, mode),
                    )
                    cur.execute(
                        """UPDATE balance
                        SET balance = balance - %s, money_in_stock = money_in_stock + %s
                        WHERE id = 1
                        """, (total_value_when_buying, total_value_when_buying)
                    )
                elif mode == 'Sale':
                    cur.execute(
                        """INSERT INTO transactions (product_id, quantity, total_price, mode, transaction_date)
                        VALUES (%s, %s, %s, %s, NOW())""", (id, abs(remaining_quantity), total_value_when_selling, mode),
                    )
                    cur.execute(
                        """UPDATE balance
                        SET balance = balance + %s, money_in_stock = money_in_stock - %s
                        WHERE id = 1
                        """, (total_value_when_selling, total_value_when_buying)
                    )
                else: pass
            else:
                print(f"No product defined at id {id}")
                return None
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Something went wrong\n DETAILS:\n{e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
change_stock(14, 20)