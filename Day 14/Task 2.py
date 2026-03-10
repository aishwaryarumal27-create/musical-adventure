import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    'Age': [25, 32, 47, 51, 62, 36, 29, 41, 38, 55],
    'Salary': [50000, 60000, 120000, 110000, 150000, 75000, 52000, 98000, 87000, 130000]
}
df = pd.DataFrame(data)
scaler_std = StandardScaler()
df_std = df.copy()
df_std['Salary'] = scaler_std.fit_transform(df[['Salary']])
scaler_mm = MinMaxScaler()
df_mm = df.copy()
df_mm['Salary'] = scaler_mm.fit_transform(df[['Salary']])
plt.figure(figsize=(15,4))
plt.subplot(1,3,1)
plt.hist(df['Salary'], bins=5, color='skyblue')
plt.title("Original Salary")
plt.subplot(1,3,2)
plt.hist(df_std['Salary'], bins=5, color='orange')
plt.title("Standardized Salary")
plt.subplot(1,3,3)
plt.hist(df_mm['Salary'], bins=5, color='green')
plt.title("Normalized Salary")
plt.show()