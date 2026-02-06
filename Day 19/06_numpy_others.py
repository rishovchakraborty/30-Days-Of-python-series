import numpy as np

# numpy zeros 
# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C'(row major mem allignmnt)/'F'(col major mem allignment))
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
# twoes = numpy_ones * 2



# Generate a random float  number
random_float = np.random.random()
random_float # 0.018929887384753874

# Generate a random float  number
random_floats = np.random.random(5)
random_floats #     array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])


# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
random_int # 4


# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
random_int #   array([8, 8, 8, 2])

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
random_int
    # array([[3, 5, 3],
    #        [7, 3, 6],
    #        [2, 3, 3]])




# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

odd_numbers = np.arange(1, 20, 2)
odd_numbers #     array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])



## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)