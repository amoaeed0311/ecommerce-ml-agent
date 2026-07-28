-- ==========================================
-- PHASE 1: DATABASE SETUP & SCHEMA DESIGN
-- ==========================================

-- 1. Create the Database
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- 2. Create the Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    signup_date DATE NOT NULL,
    region VARCHAR(50) NOT NULL,
    is_active INT DEFAULT 1 -- Useful for churn prediction later!
);

-- 3. Create the Products Table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- 4. Create the Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- ==========================================
-- INSERTING MOCK PORTFOLIO DATA
-- ==========================================

-- Insert Customers
INSERT INTO customers (customer_name, email, signup_date, region, is_active) VALUES
('Alex Johnson', 'alex.j@example.com', '2025-01-15', 'North America', 1),
('Maria Garcia', 'maria.g@example.com', '2025-02-10', 'Europe', 1),
('Liam Smith', 'liam.s@example.com', '2025-03-01', 'North America', 0), -- This user "churned"
('Yuki Tanaka', 'yuki.t@example.com', '2025-03-22', 'Asia', 1),
('Chloe Dubois', 'chloe.d@example.com', '2025-04-05', 'Europe', 1);

-- Insert Products
INSERT INTO products (product_name, category, price) VALUES
('Wireless Laptop Mouse', 'Electronics', 25.50),
('Mechanical Keyboard', 'Electronics', 85.00),
('Ergonomic Office Chair', 'Furniture', 199.99),
('Hydro Water Bottle', 'Accessories', 30.00);

-- Insert Orders
INSERT INTO orders (customer_id, product_id, order_date, quantity, total_amount) VALUES
(1, 1, '2025-05-10', 1, 25.50),
(1, 2, '2025-05-12', 1, 85.00),
(2, 3, '2025-05-14', 1, 199.99),
(3, 1, '2025-05-15', 2, 51.00),
(4, 4, '2025-05-18', 3, 90.00),
(5, 2, '2025-05-20', 1, 85.00);