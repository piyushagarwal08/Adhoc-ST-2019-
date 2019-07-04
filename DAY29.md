# DAY 29

## Notes :
  * To clear cache memory of system run command
  ```
  sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
  ```
  * Duckduckgo is worlds 3 most popular search engine

## DEEP LEARNING
  * In Machine Learning the program is not able to do any changes in the available dataset and is only able to predict on given situation
  * Deep Learning learns from dataset and do self changes in the data to learn,adjust and predict better
  * Adjusting their input as their need and outcome by changing the weights of dataset, forms a model by self adjustment until a perfect model is not achieved is a part of Deep Learning
  * Branches of DL
    1. NLP -> Neuro-linguistic Programming
      * Lexican
      * Semantic
    2. NN - > Neural Network
      * ANN
      * CNN
      * RNN
  * Standford University is majorly working over Text processing, Summarizing,Text sentiment, or Opinion Mining or Find reviews/recommendation
  * Popular NLP modules are :
    1. NLTK  -> Natural Language Tool Kit
    2. Textblob
    3. spacy

## NLTK
  * To install
  ```
  pip3 install NLTK textblob spacy
  ```
  * download all the data from standford (3.5G)

## Web Scraping

  ### Requirements
    * website is hosted somewhere
    * web crawler and web spyder
    * most powerful crawler is google bot , it moves to every website in every 2 hr to refresh its index table
  ### practice site for web scraping
    * Wiki
    * Britanika
    * php.net
  ### Parser
    * Use BeautifulSoup(https://www.crummy.com/software/BeautifulSoup/bs4/doc/), to install
    ```
    pip3 install bs4
    ```
    * to install parser
    ```
    apt-get install python-html5lib
                or
    pip3 install html5lib
    ```
    *
## Tokenization
  * DATA can be divided into 3 categories :
    1. sentence
    2. words
    3. character
  * this concept is based on making a list by seperating the words or sentences

## Stemming
  * when there is a huge amount of data and need to find a specific keyword in it to be able to predict the type of text either mail or spam
  * just make a decision based on certain keyword search

## Lemmatization
  * it creates a meaningful word from a collection of words
  * Used for sentimental analysis

## Task
  * Take picture of a newspaper and extract text + apply nltk + remove stop words and plot top 10 frequency graph(cv2 + )
  * make word from a sentence
  * apply naive bayes while reading mail from program
  * find a speech of APJ abdul kalam, scrape it , tokenize it + remove stopwords and apply stemming then replace the word and save it in a new file.
  * mark a mail as a spam using python
  * SPAM and HAM detection
