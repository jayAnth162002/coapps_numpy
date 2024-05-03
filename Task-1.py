#Task 1 => Calculate the mean and standard deviation of a NumPy array.
import numpy as np
arr = np.array([1,3,5,7,9,11,13,15,17,19])
mean = np.mean(arr)
std_dev=np.std(arr)
print("Mean:",mean)
print("Standard Deviation:",std_dev)