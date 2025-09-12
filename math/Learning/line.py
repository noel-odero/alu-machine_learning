import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]

weights = [50, 78, 83, 84, 85, 87, 67, 80, 82, 79, 76, 58, 75, 78, 87, 77]

plt.plot(years, weights)
plt.xlabel("Year")
plt.ylabel("Weight")
plt.title("Weight Progression Over Years")
plt.show()