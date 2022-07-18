import numpy as np
from numpy import dot
from numpy.linalg import norm

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

def cos_sim(i, j):
    return dot(i, j.T)/(norm(i)*norm(j))
  
print(cos_sim(a, b))
