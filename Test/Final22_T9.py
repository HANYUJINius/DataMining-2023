#9번
import numpy as np

def find_number(array, i, j, k):
    array = array[i-1:j]
    array = np.sort(array)
    return array[k-1]
    
a = np.array([1, 5, 2, 6, 3, 7, 4])
print(find_number(a, 2, 5, 3))
