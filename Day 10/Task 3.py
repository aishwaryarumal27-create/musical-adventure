import pandas as pd
df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK "]
})
print("Before Cleaning:")
print(df["Location"].unique())
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()
print("\nAfter Cleaning:")
print(df["Location"].unique())