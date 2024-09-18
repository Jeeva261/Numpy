import numpy

x=numpy.array([1,2,3,4,5,6])
print(numpy.__version__)
import math

import numpy as np

# creating numpy array-ndarray (list and tuple)
x = numpy.array([1,2,3,4,5])
print(x)

# dimension (nested array)
# 0,1,2,3 dimension array
x=np.array(67)
y=np.array([1,2,3,4,5])
z=np.array([[1,2],[1,3]])
p=np.array([[[1,2],[1,3],[1,5]]])

# higer dimension
q=np.array([1,3,5,7,9],ndmin=10)
print(x.ndim)
print(y.ndim)
print(z.ndim)
print(p.ndim)
print(q.ndim)
print(x,y,z,p,q)

# dimension indexing array
# one-dimension
x=np.array([1,2,3,4])
print(x[0:7])

#  two-dimension array
x=np.array([[1,2],[1,3]])
print(x[1,1])

# three-dimension array
x=np.array([[[1,2],[1,3],[1,4],[1,5]]])
print(x[0,0,1])



import numpy as np

# indexing

x=np.array([[[1,2,3],[4,5,6],[7,9,8]]])
print(x[0,1,1])

# slicing
x=np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,25]]])
print(x[0,0:3,3])

# datatype
x=np.array([1,2,3,4,5])
res=x.astype("f")
print(res)

# copy and view
x=np.array([1,2,3])
y=x.copy()
x[1]=100
print(y)
print(x)
y=x.view()
x[2]=200
print(y)
print(x)

# shapeandreshape

x=np.array([[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]])
x=np.array([1,2,5],ndmin=5)
print(x)
res=np.shape(x)
print(res)

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x.reshape(2,2,3).base)

# iterating

x=np.array([[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]])
for i in x:
    for j in i:
        for z in j:
          print(z)

for i in np.nditer(x,flags=["buffered"],op_dtypes=["S"]):
    print(i)

for i in np.nditer(x[0:2,:]):
    print(i)

for i in np.nditer(x[:,::, 1]):
    print(i)

for idi,i in np.ndenumerate(x):
    print(idi,i)

# join and split

x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

res=np.concatenate([x,y])
print(res)

res=np.vstack([x,y])
print(res)



x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
res=np.array_split(x,5)
print(res)
print(res[4])


x=np.array([1,2,3,4,3,4,5,5])
res=np.where(x%2==0)
print(res)

res=x.searchsorted(3,side="right")
print(res)

# sort and filter

x=np.array([1,5,3,2,4])
print(np.sort(x))


x=np.array([41,42,43,44])
filter_array=[]
for i in x:
    if i <= 42:
        filter_array.append(True)
    else:
        filter_array.append(False)


res=x[filter_array]
print(filter_array)
print(res)

x=np.array([1,2,3,4,5])
filter_arry=x%2==1
print(filter_arry)
print(x[filter_arry])