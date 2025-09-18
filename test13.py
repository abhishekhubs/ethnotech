import matplotlib.pyplot as plt
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
plt.plot(arr1,arr2, ls='--', marker='o', color='hotpink', label='line1',mec='blue', mew=2, ms=10)
plt.show() 
plt.xlabel('X-axis')
plt.ylabel('Y-axis')        