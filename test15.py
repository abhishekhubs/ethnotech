import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#diplaying all the sepal or petal length(or both)
ir=pd.read_csv("IRIS.csv")
print(ir.head())
print(ir.info())
plt.plot(ir["sepal_length"],'*',color='r',ms=5)
plt.plot(ir["petal_length"],'*',color='b',ms=6)
plt.plot(ir["sepal_width"],'*',color='g',ms=7)
plt.plot(ir["petal_width"],'*',color='y',ms=8)
plt.scatter(ir["sepal_length"],ir["petal_length"])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Scatter Plot of Sepal Length vs Petal Length")
plt.grid(True)
plt.show()
print(ir)