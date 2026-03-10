import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
skewed_data = np.random.exponential(scale=50, size=10000)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(skewed_data, size=30, replace=True)
    sample_means.append(np.mean(sample))
plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution of Sample Means (Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()