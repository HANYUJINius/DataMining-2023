#7번
import numpy as np

a = np.ones((2,3), dtype = int)
b = np.full((2,3),5, dtype = int)

c = a + b
print(c)
