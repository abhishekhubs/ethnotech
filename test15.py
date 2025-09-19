import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={"Name":["A","B","C","D","E","F"],"Values":[8,9,10,11,12,7]}
df=pd.DataFrame(data)
arr2=np.array(df["Values"])
plt.pie(arr2,labels=df["Name"],explode=(0.1,0.1,0.1,0.1,0.1,0.1), shadow=True , startangle=90)
plt.show()