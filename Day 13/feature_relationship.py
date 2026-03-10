import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [800, 1200, 1500, 1800, 2200, 2500, 3000, 3500],
    "Price": [150000, 200000, 250000, 280000, 350000, 400000, 480000, 550000],
    "City": ["A", "A", "B", "B", "C", "C", "A", "B"]
}
df = pd.DataFrame(data)
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()
correlation = df["SquareFootage"].corr(df["Price"])
print("Correlation between SquareFootage and Price:", correlation)