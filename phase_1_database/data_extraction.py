import pandas as pd
from sqlalchemy import create_engine

# Make sure DB_NAME uses the underscore!
DB_USER = "root"
DB_PASS = "12345"  # Replace with your MySQL password
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"  # <-- MUST match the schema name in MySQL Workbench!

# Create SQLAlchemy connection engine
connection_string = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(connection_string)

# Query to join your tables
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

# Extract into Pandas DataFrame
df = pd.read_sql(query, engine)

print("--- Pipeline Success! Here is your extracted data: ---")
print(df)