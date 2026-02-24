import numpy as np
import time

np_array = np.arange(1, 50001)
py_list = list(range(1, 50001))

# Repeat many times for accurate timing
repeat = 100

# NumPy timing
start = time.time()
for _ in range(repeat):
    np_sum = np.sum(np_array)
np_time = time.time() - start

# Python timing
start = time.time()
for _ in range(repeat):
    py_sum = sum(py_list)
py_time = time.time() - start

print("NumPy sum:", np_sum)
print("Python sum:", py_sum)
print("NumPy time: {:.4f} seconds".format(np_time))
print("Python time: {:.4f} seconds".format(py_time))

faster = py_time / np_time
print("NumPy is {:.1f}x faster".format(faster))