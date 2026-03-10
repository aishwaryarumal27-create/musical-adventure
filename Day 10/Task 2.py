import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': ['$700', '$150', '$300'],
    'Date': ['2026-03-01', '2026-03-02', '2026-03-03']
}
df = pd.DataFrame(data)
print("Initial data types:")
print(df.dtypes)
df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)
df['Date'] = pd.to_datetime(df['Date'])
print("\nData types after conversion:")
print(df.dtypes)
print("\nCleaned DataFrame:")
print(df)