import numpy as np

# Create NumPy array
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# Print arrays
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

# Calculate average in Fahrenheit (rounded to 1 decimal place)
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)
print("Average Fahrenheit:", avg_fahrenheit)