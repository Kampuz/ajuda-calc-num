import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return np.exp(-x) - x

# Create x values
x = np.linspace(-2, 3, 1000)
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = e^x - x')
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
plt.grid(True, alpha=0.3)

# Labels and title
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Plot of f(x) = e^x - x', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)

# Display the plot
plt.tight_layout()
plt.show()