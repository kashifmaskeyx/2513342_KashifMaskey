import time
import numpy as np

N = 1_000_000

#addition
list1 = list(range(N))
list2 = list(range(N))

t1 = time.time()
a = [list1[i] + list2[i] for i in range(N)]
print("List add:", time.time() - t1)

arr1 = np.arange(N)
arr2 = np.arange(N)

t2 = time.time()
b = arr1 + arr2
print("NumPy add:", time.time() - t2)

#multiplication
t3 = time.time()
c = [list1[i] * list2[i] for i in range(N)]
print("List multiply:", time.time() - t3)

t4 = time.time()
d = arr1 * arr2
print("NumPy multiply:", time.time() - t4)

#Dot product
t5 = time.time()
s = 0
for i in range(N):
    s += list1[i] * list2[i]
print("List dot:", time.time() - t5)

t6 = time.time()
f = np.dot(arr1, arr2)
print("NumPy dot:", time.time() - t6)

#matrix multiplication
A = [[1]*1000 for _ in range(1000)]
B = [[1]*1000 for _ in range(1000)]

t7 = time.time()
C = [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
print("List matrix multiply:", time.time() - t7)

A2 = np.array(A)
B2 = np.array(B)

t8 = time.time()
D = A2.dot(B2)
print("NumPy matrix multiply:", time.time() - t8)
