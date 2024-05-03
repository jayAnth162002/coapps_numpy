#Task 2 => Generate a random matrix of size 5x5 and then find the minimum and maximum values along each row and column.
import numpy as np
random_matrix = np.random.rand(5,5)
print("Random Matrix:")
print(random_matrix)

min_per_row =np.amin(random_matrix, axis=1)
max_per_row =np.amax(random_matrix, axis=1)

print("Minimum along each row",min_per_row)
print("Maximum along each row",max_per_row)

min_per_col = np.amin(random_matrix, axis=0)
max_per_col = np.amax(random_matrix, axis=0)

print("Minimum along each column:", min_per_col)
print("Maximum along each column:", max_per_col)