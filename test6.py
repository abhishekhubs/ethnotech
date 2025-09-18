import pandas as pd
import numpy as np

a = {
   "customerID":[1,2,3,4,5,6,7,8,9,10],
   "FirstName":["john","Jane","BOB","john","alice","\"Maria\"","Tom","Sara","CHEN","John"],
   "LastName":["doe","Smith","WILLIAMS","doe",np.nan,"Garcia","O'Malley",np.nan,"WANG","van Dyke"],
   "Age":[28.0,"NaN",45.0,28.0,34.0,29.0,41.0,29.0,np.nan,50.0],
   "City":["New York","los angeles",np.nan,"New York","San Fransciso","MIAMI","Boston","Seattle",np.nan,"St.Louis"],
   "SignUpDate":["01/05/2023","2023-02-22","15/03/2023","01/05/2023","04-18-2023","2023/07/01","12-31-2022","06/15/2023","05-05-2023","07/04/2023"]
}

s = pd.DataFrame(a)
print(s)

# remove duplicates (all cols)
s = s.drop_duplicates(inplace=False)
print("\nAfter removing duplicates:")
print(s)

# remove duplicates by FirstName + LastName
s = s.drop_duplicates(subset=['FirstName','LastName'], keep='first', inplace=False, ignore_index=True)
print("\nAfter removing duplicates by name:")
print(s)

# fix names
s['FirstName'] = s['FirstName'].str.title().str.replace('"','', regex=False).str.strip()
s['LastName'] = s['LastName'].str.title().str.replace("'","", regex=False).str.strip()
print("\nAfter fixing names:")
print(s)

# fix Age (convert to numeric + fill NaN with mean)
s['Age'] = pd.to_numeric(s['Age'], errors='coerce')   # convert "NaN" string to np.nan
s['Age'] = s['Age'].fillna(s['Age'].mean().round())

# fix City (title case, remove dots, handle NaN safely)
s['City'] = s['City'].fillna("").str.title().str.replace('.','', regex=False).str.strip()
print("\nAfter cleaning Age and City:")
print(s)
#select date filter
s['SignUpDate'] = pd.to_datetime(s['SignUpDate'], errors='coerce', dayfirst=False)
s = s[s['SignUpDate'] >= '2023-03-01']    
print("\nAfter filtering by SignUpDate:")
print(s)