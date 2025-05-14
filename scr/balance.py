from database import get_connection

def set_balance():
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO balance (id, balance, money_in_stock) 
                   VALUES (%s, %s, %s) 
                   ON CONFLICT (id) DO NOTHING""",  
                (1, 0, 0)
            )
            conn.commit()  
    except Exception as e:
        print(f"❌ Failed to set up balance\n{e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def update_balance(balance):
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """UPDATE balance SET balance = balance + %s WHERE id = 1""",(balance,)
            )
            if balance > 0:
                reason = "Additional Funds"
                cur.execute(
                    """INSERT INTO balance_adjustments (amount, reason, adjustment_date)
                    VALUES (%s, %s, NOW())""", (balance, reason))
            elif balance < 0:
                reason = "Withdrawal"
                cur.execute(
                    """INSERT INTO balance_adjustments (amount, reason, adjustment_date)
                    VALUES (%s, %s, NOW())""", (abs(balance), reason))
            conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        print(f'Somthing failed while updating balance {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def check_balance():
    conn = None
    cur = None
    try:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM balance WHERE id = 1")
            data = cur.fetchone()
            return data
    except Exception as e:
        print(f"Failed to check balance\n{e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
