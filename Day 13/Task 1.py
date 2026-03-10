import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
data = {
    'Price': [250000, 300000, 275000, 400000, 500000, 320000, 280000, 450000, 380000, 600000],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York']
}
df = pd.DataFrame(data)
sns.histplot(df['Price'], kde=True)
plt.title("Price Distribution with KDE")
plt.show()
print("Skewness:", skew(df['Price']))
print("Kurtosis:", kurtosis(df['Price']))
sns.countplot(x=df['City'])
plt.title("City Count Plot")
plt.show()