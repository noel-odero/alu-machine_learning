import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()
years = [2006 + x for x in range(16)]

weights = [50, 78, 83, 84, 85, 87, 67, 80, 82, 79, 76, 58, 75, 78, 87, 77]

plt.plot(years, weights, color="#444444", linestyle='--', marker='.')

weights_2 = [51, 98, 83, 84, 85, 87, 87, 80, 100, 79, 76, 58, 75, 78, 87, 77]
plt.plot(years, weights_2, "b", marker='o', lw=3)

plt.legend(['first weight', 'second weight'])
# plt.tight_layout()
plt.grid()
plt.xlabel("Year")
plt.ylabel("Weight")
plt.title("Weight Progression Over Years")
plt.show()