import pandas as pd
import os
data = {
    'OrderID': [101, 102, 103, None, 105, 102],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob'],
    'Amount': [250, None, 150, 200, None, None]
}
df = pd.DataFrame(data)
csv_path = os.path.join(os.getcwd(), 'customer_orders.csv')
df.to_csv(csv_path, index=False)
print(f"customer_orders.csv created at: {csv_path}\n")
df = pd.read_csv(csv_path)
print("Original DataFrame:")
print(df)
print("\nOriginal shape:", df.shape)
print("\nMissing values per column:")
print(df.isna().sum())
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
df_cleaned = df.drop_duplicates()
print("\nShape after cleaning:", df_cleaned.shape)
print("\nCleaned DataFrame:")
print(df_cleaned) 