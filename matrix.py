import numpy as np

#dimensi 2 kali 
np.random.seed(4)
a = np.random.randint(0,10 ,(2, 3))
#dimensi 3 kali 4
b = np.random.randint(0 ,10 , (3, 4))


# perkalian matrix
c = np.matmul(a, b)
print("Matrix a:\n", a)
print("Matrix b:\n", b)
print("Matrix a * b:\n", c)


