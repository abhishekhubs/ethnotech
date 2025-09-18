#pandas and numpy
import pandas as pd
import numpy as np
#using np.nan to create missing values
data={
    "customer_id":[1,2,3,4,5,6,7,8,9,10],
    "firstname":["Abhishek","John","Smith","David","Sam","Rocky","Tony","Stark","Bruce","Wayne"],
    "lastname":["Shrivastav","Wick","Wayne","Banner","Stark","Wayne","Rogers",np.nan,"Wayne","Banner"],
    "age":[24,30,35,40,28,33,np.nan,31,38,45],
    "city":["Indore","New York","Gotham",np.nan,"Gotham","New York","Los Angeles","New York","Gotham","New York"],
    "signup_date":["2022-01-01","2021-05-15","2020-07-20","2019-11-30","2021-03-25","2020-12-10","2022-02-14","2018-09-05","2019-06-18","2021-08-22"]
}
print(pd.DataFrame(data))
a1=[1,2,3,4,5,6,7,8,9,10]
num2=np.array(a1)
# print(num2)
# print(num2.shape)
# print(num2.dtype)
# print(num2.ndim)
# print(num2.nbytes)
# print(num2[1:4])
# print(num2[-1])
# print(num2[3:])
# print(num2[[0,2]])
#print two dimensional array
a2=[[1,2,3],[4,5,6],[7,8,9]]
num3=np.array(a2) 
print(num3)