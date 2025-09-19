import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ir=pd.read_csv("IRIS.csv")
print(ir.head())
print(ir.info())

# plt.bar(ir["species"],ir["sepal_length"],color=['red','blue','green'])
# plt.xlabel("Species")
# plt.ylabel("Sepal Length")
# plt.title("Bar Chart of Species")
#do with horizontal bar chart
# plt.barh(ir["species"],ir["sepal_length"],color=['red','blue','green'])
# plt.xlabel("Sepal Length")
# plt.ylabel("Species")
# plt.title("Horizontal Bar Chart of Species")
# plt.show()
#do with histogram
# plt.hist(ir["sepal_length"],bins=10,color='purple',edgecolor='black')
# plt.xlabel("Sepal Length")
# plt.ylabel("Frequency")
# plt.title("Histogram of Sepal Length")
# plt.show()