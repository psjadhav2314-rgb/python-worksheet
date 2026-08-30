import numpy as np
import random as r

from numpy.f2py.symbolic import normalize
from numpy.random.mtrand import seed

# - Matrix Transformation
# Create a 5×5 NumPy array filled with random integers between 1 and 100.
# - Replace all even numbers with 0.
# - Replace all odd numbers with 1.
# - Show the transformed matrix.
seed(1)
m = np.random.randint(1,100,(5,5))
print(np.where(m%2 == 0,0,1))

# - Diagonal Operations
# Generate a 6×6 matrix of sequential numbers (from 1 to 36).
# - Extract the main diagonal.
# - Extract the anti-diagonal (top-right to bottom-left).
# - Compute the sum of both diagonals.

d = np.arange(1,37,1).reshape(6,6)
a =d.diagonal()
b = np.diag(np.fliplr(d))
print(np.sum(a+b))

# - Sorting & Indexing
# Create a 1D NumPy array of 15 random integers between 10 and 99.
# - Sort the array in ascending order.
# - Find the indices of the three largest values.
# - Replace those three largest values with -1.

n = np.random.randint(10,99,15)
print(n)
arr = np.copy(n)
arr[np.argsort(n)[-3:]] = -1
print(arr)

# - Block Matrix Construction
# Build a block matrix using NumPy:
# [[A, B],
#  [C, D]]
# - where A, B, C, D are 2×2 matrices filled with different constant values (e.g., A=1s, B=2s, etc.).
# - Show the final 4×4 block matrix.

n1 = np.ones((2,2),dtype=int)
print(n1)
n2 = np.full((2,2),2,dtype=int )
n3 = np.full((2,2),3,dtype=int )
n4 = np.full((2,2),4,dtype=int )
print(np.vstack((np.hstack((n1,n2)),np.hstack((n3,n4)))))

# - Statistical Analysis
# Generate a 100-element NumPy array of random floats between 0 and 1.
# - Compute mean, median, variance, and standard deviation.
# - Find the 10th and 90th percentile values.
# - Normalize the array so that its mean becomes 0 and standard deviation becomes 1.

stat = np.random.rand(5,2)
print("mean : ",np.mean(stat))
print(np.median(stat))
print(np.std(stat))
print(np.var(stat))
print(np.percentile(stat,10))
print("90% :",np.percentile(stat,90))
print(stat)
normalize = (stat - np.mean(stat)) / (np.std(stat))
print(normalize)