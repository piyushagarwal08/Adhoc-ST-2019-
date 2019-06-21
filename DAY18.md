# DAY 18

## Notes
  * DecisionTree rememebers its output
  * DecisionTree is a classifier not an algo
  * It works on the algo of ID3 and CART
  * Study that what is ID3 and CART and graphviz.
  * DecisionTree makes different cases and check the features of objects one by one
  * out of All features DecisionTree selects one feature and makes and checks all possible combinations
  * graphviz(or graphwizard) is used or can be to findout which feature is placed at the top DecisionTree
  * more the features, better the data
  * sklearn provides some datasets for learning of students
  * before working on any data we need to understand each and every column details
  * if data is huge , keep a practice of breaking a dataset into two pieces,
    1. training data
    2. testing data
  * Example: if you have 1000 rows of data break the dataset into 990 rows and 10 rows , and use 990 rows for training and 10 left for testing .


## Real Data use of DecisionTree
  * Cancer
  * House Price Prediction
  * Type of flower
  * Number identification


## IRIS (DataSet)
  * iris in itself is a plant found in ireland used for medicinal purposes
  * iris plant has more then 15+ categories and university of california is working on 3 of such
    1. setosa
    2. versicoba
    3. virginica
  * it contains features = ['sepal-length','sepal-width','petal-length', 'petal-width']

  ```
  from sklearn.model_selection import train_test_split
  ```
it collects data randomly from given data set with out any kind of order

  ```
  train_Data,test_Data,answer_train,answer_test = train_test_split(features,label,test_size=0.1

    train_Data = 90%
    test_Data = 10%
    ans_train = 90%
    ans_test = 10%
    because test size is 0.1

  ```
