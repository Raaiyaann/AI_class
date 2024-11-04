import numpy as np

#dimensi 2 kali 3
a = np.random.rand(2, 3)
#dimensi 3 kali 4
b = np.random.rand(3, 4)

# perkalian matrix
c = np.dot(a, b)
print("Matrix a:\n", a)
print("Matrix b:\n", b)
print("Matrix a * b:\n", c)


