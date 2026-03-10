import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
trend_months = [1, 2, 3, 4, 5]
trend_values = [200, 400, 350, 500, 600]
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category Sales")
plt.subplot(1, 2, 2)
plt.plot(trend_months, trend_values)
plt.title("Revenue Trend")
plt.tight_layout()
plt.show()