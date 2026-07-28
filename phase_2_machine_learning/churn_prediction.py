import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import create_engine

# 1. Connection settings
DB_USER = "root"
DB_PASS = "12345"  # <-- Make sure this is your real password!
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"

print("1. Connecting to MySQL...")
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 2. Extract Data
print("2. Querying customers & orders data...")
query = """
SELECT 
    c.customer_id,
    c.region,
    c.is_active,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.quantity), 0) AS total_quantity,
    COALESCE(SUM(o.total_amount), 0) AS total_spend
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.region, c.is_active;
"""
df = pd.read_sql(query, engine)

# 3. Model Training
print("3. Preprocessing and training Random Forest model...")
df_encoded = pd.get_dummies(df, columns=["region"], drop_first=True)
X = df_encoded.drop(columns=["customer_id", "is_active"])
y = df_encoded["is_active"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 4. Generate Predictions
y_pred = model.predict(X)
churn_probabilities = model.predict_proba(X)[:, 0]

df_results = pd.DataFrame(
    {
        "customer_id": df["customer_id"],
        "predicted_is_active": y_pred,
        "churn_risk_score": np.round(churn_probabilities, 2),
    }
)

# 5. Export directly to MySQL
print("4. Writing 'churn_predictions' table to MySQL...")
df_results.to_sql(
    name="churn_predictions", con=engine, if_exists="replace", index=False
)

print("\n" + "=" * 50)
print("SUCCESS: Table 'churn_predictions' successfully written!")
print("=" * 50)
print(df_results)