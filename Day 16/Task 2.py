import pandas as pd
import numpy as np
data = {
    'Student': ['Adarsh', 'Balaji', 'Chaitra', 'Dinesh', 'Ezra', 'Fanish', 'Ganesh', 'Harish', 'Isha', 'Jatin'],
    'Score': [85, 92, 88, 95, 70, 60, 99, 87, 82, 150]
}
df = pd.DataFrame(data)
mean = df['Score'].mean()
std = df['Score'].std()
df['z_score'] = (df['Score'] - mean) / std
outliers = df[np.abs(df['z_score']) > 3]
print("Dataset with Z-scores:")
print(df)
print("\nOutliers (|Z| > 3):")
print(outliers)