import matplotlib.pyplot as plt
import numpy as np

# Define the line y = mx + b
m = 19
b = 15

x = np.linspace(-5, 5, 100)
y = m * x + b

# Plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f"y = {m}x + {b}", color="blue")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.scatter(0, b, color="red", label=f"y-intercept (0, {b})")
plt.title("Graph of y = mx + b")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
