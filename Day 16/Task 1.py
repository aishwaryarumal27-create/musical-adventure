import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
np.random.seed(42)
normal_data = np.random.normal(loc=170, scale=10, size=1000)
right_skewed_data = np.random.exponential(scale=50000, size=1000)
left_skewed_data = 100 - np.random.exponential(scale=10, size=1000)
datasets = {
    'Normal Heights': normal_data,
    'Right-Skewed Incomes': right_skewed_data,
    'Left-Skewed Test Scores': left_skewed_data
}
for name, data in datasets.items():
    df = pd.DataFrame(data, columns=['Value'])
    sns.histplot(df['Value'], kde=True)
    plt.title(name)
    plt.savefig("plot1.png")    
    mean = df['Value'].mean()
    median = df['Value'].median()
    print(f"{name} - Mean: {mean:.2f}, Median: {median:.2f}")
    if mean > median:
        print("Right-Skewed\n")
    elif mean < median:
        print("Left-Skewed\n")
    else:
        print("Approximately Normal\n")