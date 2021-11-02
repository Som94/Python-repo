#Please understand and execute it

 

#Numy_demo1.py

 

import numpy as np

#arr = numpy.array([1, 2, 3, 4, 5])

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# which type/version of Numpy I am using

print(np.__version__)

# The array object in NumPy is called::::  ndarray.

print (type(arr))

# we can convert tuple also to an ndarray

# how to do it?

arr1 = np.array((1, 2, 3, 4, 5))

print(arr1)

print (type(arr1))

# 2D array

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

 

print(arr_2d)

# 3D array

print()

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

 

print(arr_3d)

print ('below is  array dim description ....')

print (arr_2d.ndim)

print (arr_3d.ndim)

 

arr_n_dimension = np.array([1, 2, 3, 4], ndmin = 4)

print('arr_n_dimension ::: ' ,arr_n_dimension)

print (arr_n_dimension.ndim)

 

arr_quiz = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# wish to print 8, what needs to be done

print(' is it 8 ??? ', arr_quiz[1,2])

# what is the output of the below

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print (arr)

print(arr[0, 1, 2])

arr[0, 1, 2] = -99

print (arr)

print (arr.ndim)

# what is the output ?

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

print(arr[::2])

arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[16, 17, 18, 19, 20]]])

# output should be say 7 8 9 ??

print ('shreya ',arr_quiz[1,3::])

print('ranjith ' , arr_quiz[1][1:4:1])

print('another way for ranjith ' , arr_quiz[1,1:4])

print ('ranjith soln ' , arr[0,2:])

# watch

arr = np.array([1, 2, 3, 4,'Uday',True,-19.5,None], dtype='S')

print(arr)

print(arr.dtype)

# how to duplicate the contents  of  one array to another ???

arr = np.array([1, 2, 3, 4, 5])

#x = arr.copy()

# arr and x are SEPERATE entities

 

# instead of copy you use view

# when view () is used arr and x are NOT SEPERATE entities,

# they are same location reference by two handles

x = arr.view()

arr[0] = 42

print('original ',arr)

print('copied is ',x)

# arr and x are SEPERATE entities

# in array what is the concept of shape attribute

arr = np.array([[1, 2, 3, 4,55], [5, 6, 7, 8,56],[11, 12, 13, 14,57]])

tup1  = arr.shape

print ('number of rows are ', tup1[0])

print ('each row has ',tup1[1])