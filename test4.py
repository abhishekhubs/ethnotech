#only pandas
import pandas as pd
data={
    "customer_id":[1,2,3,4,5,6,7,8,9,10],
    "firstname":["Abhishek","John","Smith","David","Sam","Rocky","Tony","Stark","Bruce","Wayne"],
    "lastname":["Shrivastav","Wick","Wayne","Banner","Stark","Wayne","Rogers","Stark","Wayne","Banner"],
    "age":[24,30,35,40,28,33,29,31,38,45],
    "city":["Indore","New York","Gotham","New York","Gotham","New York","Los Angeles","New York","Gotham","New York"],
    "signup_date":["2022-01-01","2021-05-15","2020-07-20","2019-11-30","2021-03-25","2020-12-10","2022-02-14","2018-09-05","2019-06-18","2021-08-22"]
}
print(pd.DataFrame(data))      