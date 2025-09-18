import pandas as pd
#insert only one record
student= {
    "sid":[1],
    "name":["abhishek"],
    "age":[21],
    "gpa":[7.5]
}
df=pd.DataFrame(student)
print(df)