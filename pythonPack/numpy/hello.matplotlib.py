import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,5)
y = np.arange(1,5)
plt.plot(x,y)
plt.xlabel("Numbers")
plt.title("Test")
plt.show()


fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.


