#testing numpy & scipy
import numpy as np
from scipy import stats

my_array = np.array([1,2,3])
print (my_array)
print (type(my_array))

m = np.array( [ [1,2], [3,4], [5,6] ] )
print (m.shape)
print (np.mean(m))


sample = [1, 1, 1, 2, 3, 4, 5]
stats.mode(sample)

print (stats.mode(sample).count)
