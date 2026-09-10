#Exercise 2.6
import numpy as np
import matplotlib.pyplot as plt

# Create x array from -5 to 5 with 100 points
x = np.linspace(-5, 5, 100)

# y = 3x + 4
y1 = 3 * x + 4
# y = 2x^2 + 1
y2 = 2 * (x**2) + 1
# y = x^3 + 9
y3 = (x**3) + 9

# Plot the functions
plt.plot(x, y1, color='green', label='y = 3x + 4')
plt.plot(x, y2, color='blue', label='y = 2x^2 + 1')
plt.plot(x, y3, color='red', label='y = x^3 + 9')

plt.title('Plot of Multiple Math Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
