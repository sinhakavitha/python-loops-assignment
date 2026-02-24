import numpy as np

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# Shape
print("Shape:", scores.shape)

# Total elements
print("Total elements:", scores.size)

# Highest score
print("Highest score:", np.max(scores))

# Lowest score
print("Lowest score:", np.min(scores))

# Range
print("Range:", np.max(scores) - np.min(scores))