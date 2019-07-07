# DAY 31

## NOSQL
  * works on distributed system
  * no static structure
  * the schema is dynamic in nature and any type of data can be stored
  * multiple hard diska are connected with the systems which are in sync with each other
  * single query is subdivided into number of systems which in collaboration provides the output within milliseconds
  * the first nosql made by google is ```google big table```
  * google has its cache server at various ISP all over the world which provides data from local area easily
  * mysql and oracle are row oriented databases and read data row wise even when using aggregate functions
  * NOSQL is divided into 4 categories:
    1. Document Oriented NOSQL - > britannica,wiki,stack overflow are website that can be made using NOSQL . example(MongoDB,CouchDB)
      * MongoDB is a document Oriented NOSQL
    2. Column oriented database -> it is generally used for aggregation or calcultaion purpose.
      * Example ( google Big table, DynamoDB , Hbase, cassendra)
      * Hbase and cassendra are open source
      * worlds 2nd most data base is cassendra
      * It read data bases on column
    3. Key Value type NOSQL - > used mostly in cache
      * Redis and mem cached are a key-value pair oriented database
    4. Graph Database (complex)
      * Blockchain is a tech made using Graph Database
      * Neo4j is a database based or graph architecture
      * Blockchain is not hackable because it works on token system type where single data packet is transferred from one node to other to be transferred from source to destination

## DynamoDB ( TOO COSTLY ~ Beware )
  * Biggest customer is PUBG
  * It can be integrated easily with any programming language
  * it has no need for DBA or basically no need of maintainence

## AWS LAMBDA
  * it is used in collaboration with DynamoDB
  * it can dynamically add data resources and store dynamically in DynamoDB easily
  * thus LAMBDA provides a user with both platform and resources ad developer only needs to focus over coding
----

# Tensorflow
  * the team of google 'Google Brain Team' created Tensorflow
  * Main use of Tensorflow is to build up a neural network / image classification or maths calcultaion
  * using the Tensorflow we can do both classification and regression
  * Neurons are a part of human body having 3 parts
    1. dendrite (takes input to a neuron )            ``` ~~~~()```
    2. cell body ( processing takes place )
    3. axon ( output to neuron )
  * work of axon is to transfer data from neuron1 to neuron2
  * Neural Network is a collection of neurals that are neurons
  * Artificial Neural Network (ANN) - > in this no of neurons can be decided by us
```
              input     process    output
              --@ - - - - >@ - - -  |
dendrites --@ - - - - >@ - - - >@   -- output
              --@ - - - - >@ - - -  |
```

* input is the no of layers to be given to a neural network
* there can be <b>N</b> no of neurons in a single layer
* there are 3 things in a neural network :
 1. input layer - > takes the inputs
 2. hidden layer - > processing layer
 3. output - > its not classified as a layer


* activation function - > mathematical function used by a layer to process the data present with it,the information recieved at a certain layer is required to be processed and need to be send further
* input layer should have no of nodes equal to no of inputs or attributes
* input layer never processes, its work is to collect data and pass it to hidden layer to be processed
* single neuron can be connected with each and every node of hidden layer
* more the hidden layer more the CPU,GPU or TPU will be required

* basic activation functions being used (Recommended by Google) are :
  1. Threshold Function -> when decision to be taken is yes or no

  2. Sigmoid function - > generally used in final layer of neural network to predict something
  3. Rectifier function - > find the max of output
  4. Hyperbolic Function - > value range is from -1 to 1


* If ANN has more then 2 hidden layers , its known as Deep Neural Network

* Cost Function is used to find the difference between the actual output and predicted output

```
0.5 * root( (actual - predicted) ** 2)
```
* Use cases of NN:
  1. Performance search
  2. Voice processing
  3. Self driving car
  4. Computer games


* Father of Deep Learning is Geoffrey Hinton
* Weights  -> multiplying the actual inputs in a way that it doesn't change the value of data but provides the accurate output
* the weights must have value between 0 and 1 such that the change in attributes is not significant by itself
* The work of neural network is to change the value of weights in case the output is not appropriate to cost function and reprocesses until a perfect output is obtained
* Epoch - > Epoch is defined as the no of times the complete ANN process is completed  
* batch size - > to pick some amount of data from some an attribute
