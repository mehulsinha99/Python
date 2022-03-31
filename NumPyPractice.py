import numpy as np
from skimage import data
astranaut=data.astronaut()
print(astranaut)
print(astranaut.size)

print(np.__version__)
print(np.show_config())


'''
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 0
print(arr)
print(x)

arr1 = np.array([6,7,8,9,10])
x1 = arr1.view()
arr1[0] = 1
print(arr1)
print(x1)


arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)
    
import timeit

# vectorized sum
print(np.sum(np.arange(15000)))

print("Time taken by vectorized sum : ", end="")
%timeit np.sum(np.arange(15000))

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(2,2,3))
print(arr)
print(type(arr))
print(arr[0])
print(arr[1:5])

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
print(arr3)

newarr = np.array_split(arr,3)
print(newarr)
x = np.where(arr == 3)
print(x)
arr4 = np.array([5,7,3,2,9])
print(np.sort(arr4))

a = np.array([('Sana',2,21.0),('Mansi',7,29.0)],
             dtype=[('name',(np.str_,10)),('age',np.int32),('weight',np.float64)])
#sorting ac toname
b = np.sort(a,order='name')
print("sorting ac to name",b)

c = np.sort(a,order='age')
print("sorting ac to age",c)


'''