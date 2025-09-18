import pandas as pd
data ={
    "studentID":[1,2,3,4,5],
    "FirstName":["john","Jane","BOB","john","alice"],
    "LastName":["doe","Smith","WILLIAMS","doe","alice"],
    "Age":[28.0,"NaN",45.0,28.0,34.0],
    "department":["CSE","ECE","CSE","CSE","ECE"],
    "gpa":[3.5,8,4.0,3.8,3.6]

}
df=pd.DataFrame(data)
print(df)
#sorting by multiple column(department,then gpa descending)
print("\nAfter sorting by department and gpa:")
df=df.sort_values(by=['department','FirstName'],ascending=[True,False])
print(df)

#df=df[(df['department']=='CSE') & (df['gpa']>=3.6)]
#print(df)
# print(df.iloc[3:])
# print(df.T)
#appending
student= {
    "sid":[1],
    "name":["abhishek"],
    "age":[21],
    "gpa":[7.5]
}
# df=pd.DataFrame(student)
# print(df._append(student,ignore_index=True))
#trucking 3 records
print(df.head(3))