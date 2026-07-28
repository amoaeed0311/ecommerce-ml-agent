import pandas as pd
from sqlalchemy import create_engine

# 1. Connection setup
DB_USER = "root"
DB_PASS = "12345"  # <--- Put your password here
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 2. Extract Data
query = """
SELECT 
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name,
    c.region,
    c.is_active,
    p.product_name,
    p.category,
    o.quantity,
    o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
"""

df = pd.read_sql(query, engine)

# 3. Data Cleaning & Type Conversion
df["order_date"] = pd.to_datetime(df["order_date"])
df["total_amount"] = df["total_amount"].astype(float)

# 4. Calculate Key Business Metrics (KPIs)
total_revenue = df["total_amount"].sum()
total_orders = df["order_id"].nunique()
active_customers = df[df["is_active"] == 1]["customer_id"].nunique()
churned_customers = df[df["is_active"] == 0]["customer_id"].nunique()

category_sales = (
    df.groupby("category")["total_amount"].sum().reset_index()
)

# 5. Print Executive Summary
print("\n" + "=" * 45)
print("       BUSINESS INTELLIGENCE SUMMARY       ")
print("=" * 45)
print(f"Total Revenue Generated : ${total_revenue:,.2f}")
print(f"Total Orders Processed  : {total_orders}")
print(f"Active Customers        : {active_customers}")
print(f"Churned Customers       : {churned_customers}")
print("-" * 45)
print("Sales by Category:")
print(category_sales.to_string(index=False))
print("=" * 45 + "\n")