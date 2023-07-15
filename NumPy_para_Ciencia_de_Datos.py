## NumPy Arrays

# Creating NumPy Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print (arr) # OUTPUT: [1, 2, 3, 4, 5]

arr = np.arange(0, 10, 2)
print (arr) # OUTPUT: [0, 2, 4, 6, 8]

zeros = np.zeros((3, 3))
print (zeros) 
# OUTPUT: [[0. 0. 0.]
#          [0. 0. 0.]
#          [0. 0. 0.]]

ones = np.ones((2, 4))
print (ones) 
# OUTPUT: [[1. 1. 1. 1.]
#          [1. 1. 1. 1.]]

# Array Atributes

'''
NumPy arrays have various attributes that provide useful
information about the array's shape, size, and data type. 
Somecommonly used attributes include:
shape: Returns a tuple representing the size of eachdimension of the array.
dtype: Returns the data type of the array elements.
ndim: Returns the number of array dimensions.
size: Returns the total number of elements in the array.
itemsize: Returns the size in bytes of each array element.
'''

# Indexing and Slicing Arrays

arr = np.array([1, 2, 3, 4, 5])

print (arr[0])    # Output: 1
print (arr[-1])   # Output: 5
print (arr[2:4])  # Output: [3 4]

# Array Operations

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print (arr1 + arr2)    # Output: [5 7 9]
print (arr1 * arr2)    # Output: [4 10 18]
print (arr1 ** 2)      # Output: [1 4 9]

# Broadcasting

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

print (arr1 * scalar)

# OUTPUT:
# [[2 4 6]
#  [8 10 12]]

## Array Manipulation

# Reshaping Arrays

arr = np.arange(1, 10)

reshaped = arr.reshape(3, 3)
print (reshaped)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Joining and Splitting Arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated =np.concatenate((arr1, arr2))
print (concatenated)

# OUTPUT: [[1 2 3 4 5 6]

# Changing Array Data Types

arr = np.array([1, 2, 3], dtype=np.float64)

new_arr = arr.astype(np.int32)
print (new_arr)

# OUTPUT: [[1 2 3]

# Sorting and Searching Arrays

arr = np.array([4, 2, 1, 3, 5])

sorted_arr = np.sort(arr)
print (sorted_arr)

# OUTPUT: [[1 2 3 4 5]

## Mathematical Functions

# Basic Mathematical Operations

arr = np.array([1, 2, 3])

print (np.square(arr))        # Output: [1 4 9] 
print (np.sqrt(arr))          # output: [1.           1.41421356 1.73205081]
print (np.exp(arr))           # output: [  2.71828183   7.3890561  20.08553692]

# Trigonometric Functions

arr = np.array([0, np.pi / 2, np.pi])

print (np.sin(arr))  # Output: [0.00000000e+00 1.00000000e+00 1.22464680e-16]
print (np.tan(arr))  # Output: [1.0000000e+00 6.1232340e-17 -1.0000000e+00]
print (np.tan(arr))  # Output: [ 0.00000000e+00  1.63312304e+16 -1.22464680e-16]

# Exponential and Logarithmic Functions

arr = np.array([1, 10, 100])

print (np.exp(arr))   # Output: [2.71828183e+00 2.20264658e+04 2.68811714e+43]
print (np.log(arr))   # Output: [0.         2.30258509 4.60517019]
print (np.log10(arr)) # Output: [0.  1.  2.]

# Statistical Functions

arr = np.array([1, 2, 3, 4, 5])

print (np.mean(arr))     # Output: 3.0
print (np.median(arr))   # Output: 3.0
print (np.std(arr))      # Output: 1.41421356

# Linear Algebra Operations

matrix = np.array([[1, 2],[3, 4]])

print (np.dot(matrix, matrix))  # Output: [[ 7 10]
                                #          [15 22]]
print (np.transpose(matrix))  # Output: [[1 3]
                              #          [2 4]]

## Array Input and Output

# Saving and Loading Arrays

arr = np.array([1, 2, 3, 4, 5])

np.save('array.npy', arr)
loaded_arr = np.load('array.npy')

print (loaded_arr)

# OUTPUT: [[1 2 3 4 5]

# Text File Input and Output

arr = np.array([1, 2, 3, 4, 5])

np.savetxt('array.txt', arr)

print (loaded_arr)

# OUTPUT: [[1. 2. 3. 4. 5.]]

# Binary File Input and Output

arr = np.array([1, 2, 3, 4, 5])

np.save('array.npy', arr)
loaded_arr = np.load('array.npy')

print (loaded_arr)

# OUTPUT: [1 2 3 4 5]

# Compressed File Input and Output

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

np.savez('arrays.npz', arr1=arr1, arr2=arr2)
loaded_data = np.load('arrays.npz')

print (loaded_data['arr1'])   # Output: [1 2 3]
print (loaded_data['arr2'])   # Output: [4 5 6]

## Advanced NumPy Features

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2
print (result)

# OUTPUT:
# [[11 22 33]
#  [14 25 36]]

# Array Manipulation Tricks

arr = np.array([[1, 2, 3], [4, 5, 6]])

transposed = arr.T
repeated = np.repeat(arr, 2, axis=0)
stacked = np.stack((arr, arr), axis=0)

print (transposed)
print (repeated)
print (stacked)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]]]

# Fancy Indexing and Boolean Masking

arr = np.array([1, 2, 3, 4, 5])

indices = np.array([0, 2, 4])
print (arr[indices])              # Output: [1 3 5]

mask = arr > 2
print (arr[mask])                 # Output: [3 4 5]

# Structured Arrays

dt = np.dtype([('name', np.str_, 16), ('age', np.int32), ('salary', np.float64)])
arr = np.array ([('John', 25, 5000.0), ('Alice', 30, 6000.0)], dtype=dt)

print (arr['name'])          # Output: ['John' 'Alice']
print (arr['age'])           # Output: [25 30]
print (arr['salary'])        # Output: [5000. 6000.]

# Universal Functions

arr = np.array([1, 2, 3])

print (np.add(arr, 2))         # Output: [3 4 5]
print (np.multiply(arr, 3))    # Output: [3 6 9]
print (np.sqrt(arr))           # Output: [1.           1.41421356  1.73205081]


print (np.divide(arr, 3))      # Output: [0.33333333 0.66666667 1.        ]
print (np.subtract(arr, 3))    # Output: [-2 -1  0]

## Performance Tips and Best Practices

# Vectorization

''' Non-vectorized approach '''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.zeros(3)

for i in range(3):
    result[i] = arr1[i] + arr2[i]
    
print (result)                      # Output: [5. 7. 9.]

''' Vectorized approach '''
result = arr1 + arr2
print (result)                      # Output: [5 7 9]

# Memory Efficiency

arr1 = np.array([1, 2, 3])
arr2 = arr1

''' Creating a view (no additional memory) '''
view = arr1.view()

''' Creating a copy (additional memory) '''
copy = arr1.copy()

print (arr1)         # Output: [1 2 3]
print (arr2)         # Output: [1 2 3]

print (view)         # Output: [1 2 3]
print (copy)         # Output: [1 2 3]

# Use NumPy Functions Instead of Loops

arr = np.array([1, 2, 3, 4, 5])

''' Non-vectorized approach '''
total = 0
for num in arr:
    total += num
    
print (total)             # Output: 15

''' Vectorized approach '''
total = np.sum(arr)
print (total)             # Output: 15


''' 
CONCLUSION

NumPy is a powerful library for data science, providingefficient and flexible 
data structures and functions fornumerical computing. In this practical guide, 
we covered thebasics of NumPy, including array creation, indexing and slicing, 
array operations, array manipulation, mathematical functions,input and output, 
advanced features, performance tips, andbest practices. With this knowledge, 
you can leverage NumPyto perform various data science tasks efficiently andeffectively. 
Happy coding!

'''
