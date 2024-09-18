# Create a 3x3 NumPy array and perform basic operations
import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
addition=x+2
print(addition)
sub=x-2
print(sub)
multi=x*2
print(multi)
div=x/5
print(div)
new1=np.max(x)
print(new1)
new2=np.min(x)
print(new2)
new3=np.mean(x)
print(new3)


# Write a script to find the mean, median, and standard deviation of an array.

def calculate_statistics():
    x=np.array([1,2,3,4,5,6,7,8,9,10])
    mean=np.mean(x)
    median=np.median(x)
    std=np.std(x)
    return mean,median,std