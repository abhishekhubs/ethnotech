import pandas as pd
import numpy as np
data={
    "studentID":[1,2,3,4,5],
    "studentName":["Abhishek","Joel","Darshan","Manish","Alice"],
    "USN":["4SN23CS005","4SN23CS046","4SN23CS033","4SN23CS055","4SN23CS099"],
    "Grade":[8,8.5,9,8.7,6],
    "City":["Mangalore","Mangalore","Puttur","Dharmasthala","Goa"],
    "Age":[22,20,21,20,25],
    "Gender":["Male","Male","Male","Male","others"]
}
df=pd.DataFrame(data)
print(df)
df.to_csv('cse-a', index=False)
df = pd.read_csv('cse-a')
print(df)