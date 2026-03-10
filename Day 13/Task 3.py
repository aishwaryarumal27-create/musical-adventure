import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Sales': [200, 220, 250, 300, 280, 400, 500, 450, 600, 700],
    'Advertising': [20, 25, 30, 35, 32, 40, 50, 45, 55, 65],
    'Profit': [50, 55, 60, 80, 70, 100, 120, 110, 150, 180],
    'Expenses': [150, 165, 190, 220, 210, 300, 380, 340, 450, 520]
}
df = pd.DataFrame(data)
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
high_corr = [(i, j, corr_matrix.loc[i, j]) for i in corr_matrix.columns for j in corr_matrix.columns if i != j and abs(corr_matrix.loc[i, j]) > 0.8]
print("Variable pairs with correlation > 0.8:")
for pair in high_corr[:2]:
    print(pair)
sns.boxplot(y=df['Sales'])
plt.show()