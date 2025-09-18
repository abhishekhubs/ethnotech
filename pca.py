#principle component analysis(PCA)
#used for reducing noise,visualization
import numpy as np
import pandas as pd
df = pd.read_csv('IRIS.csv')
print("sepal length mode:",df['sepal_length'].mode()[0])
print("sepal length mean:",df['sepal_length'].mean())
print("sepal length std:",df['sepal_length'].std())