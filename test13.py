import matplotlib.pyplot as plt
import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr2=np.array([1,3,5,2,4,6])
plt.barh(arr1,arr2,color='c')
plt.xlabel("Number from 1 to 6(X)")
plt.ylabel("Number from 1 to 6(Y)")
plt.title("THIS IS JUST EXAMPLE(ManePear)")
plt.hist(arr2,color='g',bins=5)
for i,j in zip(arr1,arr2):
    plt.text(j,i,str(j),va='center',fontweight='bold',color='b')
plt.show()