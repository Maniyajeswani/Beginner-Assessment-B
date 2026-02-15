CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(100),
    region VARCHAR(50),
    signup_date DATE
);

CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    product_id INT,
    quantity INT
);
