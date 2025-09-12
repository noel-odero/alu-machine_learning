import numpy as np
import matplotlib.pyplot as plt

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 70, 43, 67]

plt.bar(x, y)
plt.xlabel("Language")
plt.ylabel("Votes")
plt.title("Determining the most popular langauge")
plt.show()