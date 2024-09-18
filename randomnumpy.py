from numpy import random
import numpy as np

# mathamatical function

x=random.rand(5,5)
print(x)

x=random.randint(100)
print(x)

x=random.choice([1,2,3,4,5,6,],size=(3,5))
print(x)


# Data Distribution
p=0,1
x=random.choice([2,5,8,9],p=[0.1,0.3,0.3,0.3],size=(5,5))
print(x)

# random permulation
x=np.array([1,2,3,4,5])
random.shuffle(x)

y=random.permutation(x)
print(y)
print(x)


x=random.normal(loc=3,scale=5,size=8)
print(x)

x=random.binomial(n=10,p=0.100,size=10)
print(x)

x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],size=(3,3))
print(x)

x=random.exponential(scale=1.0,size=10)
print(x)

x=random.uniform(size=(2,3))
print(x)

x=random.logistic(loc=2,scale=5,size=10)
print(x)

x=random.poisson(lam=4,size=(5,2))
print(x)