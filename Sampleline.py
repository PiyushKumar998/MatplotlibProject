import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sine Wave", color="blue", linewidth=2)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="red", label="Scatter Points")
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar chart
categories = ["A", "B", "C", "D"]
values = [4, 7, 2, 9]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color="green")
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
