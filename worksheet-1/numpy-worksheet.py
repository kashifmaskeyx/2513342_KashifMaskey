import numpy as np

#Task1
# a = np.empty((2,2))
# print(a)

# b = np.ones((4,2))
# print(b)

# c = np.full((3,3), 5)
# print(c)

# d = np.array([[1,2],[3,4]])
# e = np.zeros_like(d)
# print(e)

# f = np.ones_like(d)
# print(f)

# g = [1,2,3,4]
# h = np.array(g)
# print(h)


#TASK2
i = np.arange(10,50)
print(i)

j = np.arange(9).reshape(3,3)
print(j)

k = np.eye(3)
print(k)

l = np.random.random(30)
print(l.mean())

m = np.random.random((10,10))
print(m.min(), m.max())

n = np.zeros(10)
n[4] = 1
print(n)

o = np.array([1,2,0,0,4,0])
print(o[::-1])

p = np.ones((5,5))
p[1:4,1:4] = 0
print(p)

q = np.zeros((8,8), int)
q[1::2, ::2] = 1
q[::2, 1::2] = 1
print(q)


#Task3
x = np.array([[1,2],[3,5]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11,12])

print(x + y)
print(x - y)
print(x * 2)
print(x**2)

print(np.dot(v,w))
print(np.dot(x,v))
print(np.dot(x,y))

print(np.vstack((x,y)))
print(np.column_stack((v,w)))

try:
    print(np.concatenate((x,v)))
except Exception as t:
    print("Shapes dont match")


# Problem 4
A = np.array([[3,4],[7,8]])
B = np.array([[5,3],[2,1]])

print(A.dot(np.linalg.inv(A)))
print(A.dot(B))
print(B.dot(A))

print((A.dot(B)).T)
print(B.T.dot(A.T))

C = np.array([[2,-3,1],
              [1,-1,2],
              [3,1,-1]])
D = np.array([-1,-3,9])

print(np.linalg.solve(C,D))
