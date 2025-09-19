import matplotlib.pyplot as plt
import numpy as np
data=["A","B","C","D"]
arr2=np.array([8,9,10,11])
plt.pie(arr2,labels=data)
plt.legend()
plt.show()
