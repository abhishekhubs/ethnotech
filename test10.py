import numpy as np
import pandas as pd
#using np.nan to create missing values
data={
    "customer_id":[1,2,3,4,5,6,7,8,9,10],
    "firstname":["Abhishek","John","Smith","David","Sam","Rocky","Tony","Stark","Bruce","Wayne"],
    "lastname":["Shrivastav","Wick","Wayne","Banner","Stark","Wayne","Rogers",np.nan,"Wayne","Banner"],
    "age":[24,30,35,40,28,33,np.nan,31,38,45],
    "city":["Indore","New York","Gotham",np.nan,"Gotham","New York","Los Angeles","New York","Gotham","New York"],
    "signup_date":["2022-01-01","2021-05-15","2020-07-20","2019-11-30","2021-03-25","2020-12-10","2022-02-14","2018-09-05","2019-06-18","2021-08-22"]
}
df = pd.DataFrame(data)
result = df[(df['age'] > 20) & (df['city'] == "New York")]
print(result)
dropnull= df.dropna()
print(dropnull)
sorted_df = df.sort_values(by='customer_id')
print(sorted_df)
grouped_df = df.groupby('city').size().reset_index(name='customer_count')
aggregated_df = df.groupby('city')['age'].mean().reset_index(name='average_age')
merged_df = pd.merge(grouped_df, aggregated_df, on='city')
final_df = pd.merge(df, merged_df, on='city', how='left')
print(final_df)
df.to_csv('customer_data.csv', index=False)
df = pd.read_csv('customer_data.csv')
print(df.head())