import pandas as pd
df =pd.DataFrame()

### merge/concat dataframes
df=df.merge(product_count,on=cols,how='left')
df=pd.concat([df,pd.get_dummies(df['City_Category'])],axis=1)



### Pandas drop duplicates or NA
cols =[]
df=df.dropna(axis=0, how='any')
df=df.drop_duplicates(cols,inplace=True) 
df=df.drop(cols,axis=1,inplace=True)

#### Pandas group by 

user_count=df[['User_ID','Product_ID']].groupby('User_ID').count().rename(columns={'Product_ID':'User_count'}).reset_index()

### Pandas one hot encoding
df=pd.get_dummies(df, columns=cols)

### Label Encoding and One hot Encoding
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(df[col].values)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)


### Scaling
from sklearn import preprocessing
X = preprocessing.scale(X)
## Normalizing
from sklearn import preprocessing
X = preprocessing.normalize(X)

### Transfrom string to date time 
import pandas as pd
col =''
df[col]=pd.to_datetime(df[col],format=('%Y-%m-%d %H:%M:%S'))
import time
time = time.strptime("30 Nov 00", "%d %b %y")
# %a	Weekday as locale’s abbreviated name.
# %A	Weekday as locale’s full name.
# %w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %d	Day of the month as a zero-padded decimal number.
# %b	Month as locale’s abbreviated name.
# %B	Month as locale’s full name.
# %m	Month as a zero-padded decimal number.
# %y	Year without century as a zero-padded decimal number.
# %Y	Year with century as a decimal number.
# %H	Hour (24-hour clock) as a zero-padded decimal number.
# %I	Hour (12-hour clock) as a zero-padded decimal number.
# %p	Locale’s equivalent of either AM or PM.
# %M	Minute as a zero-padded decimal number.
# %S	Second as a zero-padded decimal number.
# %f	Microsecond as a decimal number, zero-padded on the left.
# %z	UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
# %Z	Time zone name (empty string if the object is naive).
# %j	Day of the year as a zero-padded decimal number.
# %U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
