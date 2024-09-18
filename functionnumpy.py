# universal function
# vectorization-cpu faster
# import numpy as np
# x=[1,2,3,4,5]
# y=[5,4,3,2,1]
# z=np.add(x,y)
# print(z)
import numpy as np


# creating function in numpy

def myfun(x,y):
    return x+y

myfun=np.frompyfunc(myfun,2,1)
print(myfun([1,2,3,4,5],[6,7,8,9,10]))