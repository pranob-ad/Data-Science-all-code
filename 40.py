import matplotlib.pyplot as plt

# Enable sketch-style drawing
from matplotlib import rcParams
rcParams['path.sketch'] = (1, 100, 2)  # (scale, length of the wiggle, randomness)

days = [1, 2, 3, 4, 5, 6, 7]
gold_prices = [8975, 9923, 8765, 9115, 8931, 8769, 8721]
plt.plot(days, gold_prices, marker='o', linestyle='--', color='gold', label='Gold Prices')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.title('Gold Market Trend')
plt.legend()
plt.show()