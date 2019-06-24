# DAY 20

## Notes
  * to attach new volume in Virtual Box at run time without restarting
    we use virtIO in storage setting
  * At AWS , we can attach new volumes without rebooting or stopping the system
  * $ partprobe -> to resync all HDD in
  * mount -a -> it runs the fstab file again and mounts the HDD if not mounted
  * to permit root login on AWS , open ```/etc/ssh/sshd_config``` file and set ```permitrootlogin``` to ```yes```
  * ```lsblk --output=uuid device-name``` it gives uuid of specific HDD

## SSH
  * ssh ip-address  # it logins on other system with same user you are running this command as
  * ssh stands for Secure Shell
  * ssh -X root@ip -> used to give graphical interface to virtual box

## LVM
  * LVM stands for Logical Volume Manager
  * -l extents - > it is used to provide size in terms of extents
  ```
  lvcreate --name tech -l 30 vg-name
  ```
  * to display the content of lvm in short use ```lvs```
  * to give a physical extent size to vg group usw ``` -s ```
  ```
  vgcreate -s 16M vg-name hdd-name1 hdd-name2
  ```

# Data Engineering
  * A classifier requires an accurate data to use its processing algorithm
  * pre-processing of data before applying ML is know as Data Engineering
  * tasks in Data Engineering - >
    1. Clean
    2. Recycle
    3. Auto Fill
  * pandas is similar to SQL and basically creates its own structure called DataFrame
  * Imputer - > replacing missing numerical value with relevant data is done with the help of imputer
  * Data Processing have a branch called Dummy variable
  * Dummy cariable works in a way that it encodes the string into a array format like [1,0,0] where 1 the value in row 1 is flagged as 1 and other as 0 and length of array is equal to number of different values
  * To calculate distance KNN uses distance formula that is
  ```
  root((x1-x2) + (y1-y2) + (z1-z2))
  ```
  * Feature Scaling - > it is the method of data where we convert features in the range of each other
  e.g., 1 feature has values (27,38,59) and other one has values (10000,239999,38888) so bring both features in similar range this method is applied
  * Imputing is a part of Data Mining & Engineering


## Todays python jupyter code

```python
import pandas as pd

#Reading csv file from URL
df = pd.read_csv('http://13.234.66.67/summer19/datasets/info.csv')
df.info()
df
#seperating out data or columns
x = df.iloc[:,0:].values #values is used to give only values not headers

# To remove missing values or replacing missing values with some relevant data
df.describe() # it describes the numerical columns
from sklearn.preprocessing import Imputer
# to check data to be none in column/column oriented axis=0
# strategy is used to replace the missing value
imp=Imputer(missing_values='Nan',axis=0,strategy='mean')
# fitting columns that we want to process
impute = imp.fit(x[:,1:3]) # needs only 2d array
# fit is used to make a schema

# now for transforming the fitted columns
x[:,1:3] = impute.transform(x[:.1:3])
x  # printing the value of x, missing values are replaced by strategy

# to label any string with some int or float value
from sklearn.preprocessing import LabelEncoder
cont = LabelEncoder() # object made for country labelling

#Now applying label in column 1, that is it will replace string with integer
x[:,0] = cont.fit_transform(x[:,0])
#Now replacing label in column last, that is it will replace yes/no with 0 or 1
x[:,-1] = cont.fit_transform[:,-1]

# Now encoding first column i.e., making subcolumn of column 1
from sklearn.preprocessing import OneHotEncoder
firstcl = OneHotEncoder(categorical_features=[0]) # Defining exact column number where we want to make category

# fit_transofrm convers x into sparse matrix and toarray() convers it into  ndarray
x = firstcl.fit_transform(x).toarray()
x.astype(int) # converts the array in proper integer type

```
