import numpy

pure_python_data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
array = numpy.array(pure_python_data)
print (array)
print("There are", array.ndim, "dimensions in the array")
print("The shape of the array is", array.shape)
print("In total, there are", array.size, "values")
print("We have an array of", array.dtype)
print("Column", array[:,2])
print("Row",array[1,])
def mean_point(points):
    return
array1 = numpy.arange(9).reshape(3,3)
array2 = numpy.ones((3,3), dtype=numpy.int32)
print("array1",array1)
print("array2",array2)
print((array1*array2)/2)