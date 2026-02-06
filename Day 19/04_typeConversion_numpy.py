import numpy as np

# int to float
int_list=np.array([1,2,3,4])
print(int_list.dtype)
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr) # array([1., 2., 3., 4.])
print(numpy_int_arr.dtype)

# floar to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr

#int to bool
np.array([-3, -2, 0, 1,2,3], dtype='bool')
#    array([ True,  True, False,  True,  True,  True])


# Int to str
int_list.astype('int').astype('str')