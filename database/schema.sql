CREATE TABLE IF NOT EXISTS product (
    id BIGSERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    selling_price NUMERIC(10,2) NOT NULL CHECK (selling_price > 0),
    purchase_price NUMERIC(10,2) NOT NULL CHECK (purchase_price > 0)
);

CREATE TABLE IF NOT EXISTS inventory (
    id BIGSERIAL PRIMARY KEY,
    product_id BIGINT UNIQUE NOT NULL REFERENCES product(id) ON DELETE CASCADE,
    quantity INT NOT NULL CHECK (quantity >= 0)
);

CREATE TABLE IF NOT EXISTS transactions (
    id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL REFERENCES product(id) ON DELETE CASCADE,
    quantity INT NOT NULL CHECK (quantity > 0),
    total_price NUMERIC(10,2) NOT NULL CHECK (total_price > 0),
    mode VARCHAR(25) NOT NULL,
    transaction_date DATE DEFAULT CURRENT_DATE
);
CREATE TABLE IF NOT EXISTS balance (
    id INT PRIMARY KEY ,
    balance NUMERIC(10,2) NOT NULL CHECK (balance >= 0),
    money_in_stock NUMERIC(10,2) NOT NULL CHECK (money_in_stock >= 0)
);
CREATE TABLE IF NOT EXISTS balance_adjustments (
    id SERIAL PRIMARY KEY,
    amount NUMERIC(10,2) NOT NULL,
    reason TEXT NOT NULL,
    adjustment_date DATE DEFAULT NOW()
);
