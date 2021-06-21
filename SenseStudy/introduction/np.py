import random
import time
import numpy as np
a = []
for i in range(10000000):
    a.append(random.random())

t1 = time.time()
sum1=sum(a)
t2=time.time()

b=np.array(a)
t4=time.time()
sum3=np.sum(b)
t5=time.time()
print(t2-t1, t5-t4)

#----------------------------------------------
'''
l = [1,2,3,4]
print(l)
arr1 = np.array([1,2,3,4])
print(arr1)
arr2 = np.array([[1,2,4], [3,4,5]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)
arr3 = arr2.T
print(arr3.shape)

arr4 = np.array([1.2+2j, 2+3j])
print(arr4.real)
print(arr4.imag)

l = [1,2,3,4]
print(l*2)
print(l+l)
a = np.array([1,2,3,4])
print(a*2)
print(a+a)
'''
