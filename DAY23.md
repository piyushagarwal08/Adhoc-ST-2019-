# DAY 23

  * ifconfig```br0: ```
  * ifnet is the private ip
  * lancard of ethernet is eno1
  *  lancard of wifi is wl
  *  bridgecard is br0
  *  in exam many things are configured on br0
  * Fixing an IP is termed as static ip

## Setting up static IP
  * ping ip-address -> check if ip is working properly
  * ping server-name (if not possible then set in resolv.conf )
  * set ip
  ```
  cd /etc/sysconfig/network-scripts/
  ```
  * name of file in this directory should be ifcfg-lan_card_name
  example ifcfg-eth0
  * vi ifcfg-etho
  * change BOOTPROTO="static"
  * NAME = "lan-card-name"
  * ONBOOT = "yes"
  * in last line
  ```
  IPADDR= 192.168.10.43
  DNS=192.168.10.254 (server will be given,name-server/domain-name-server)
  NETMASK= 255.255.255.0 - > single public ip (can be taken from ifconfig)
  GATEWAY= 192.168.10.1     (ip to communicates with outside world)
  ```
  * route -n # shows the values of kernel ip routing table
  * 0.0.0.0 means anywhere
  * after configuration, reboot which must show the set ip
  * resolv.conf - > gives ip from name
  * after setting static ip
  * open ```/etc/resolv.conf```
  * nameserver ip-address-of-eth0


## Web Scrapping
  *   Web Scrapping means scrapping web data from websites leagally or illegally.
  *   Scrap means Kachra.
  *   The art of extracting useful data from web scrap data is called as Web Scrapping.
  *   To scrap data we use some liberaries to scrap data like Beautiful Soup
  *   To install beautiful soup we use
  ```
  pip3 install bs4
  ```
  *   Now first we need a request model to download web data using http/tcp protocol.
  *   To use this we need a liberary called ```requests```
  *   To install requests model use
  ```
  pip3 install requests
  ```
  *   Now Lets begin with importing the liberaries.
  ```py
  import request
  from bs4 import BeautifulSoup as bsf
  ```
  *   Now to create request we need a weburl
  ```py
  url = "https://en.wikipedia.org/wiki/Death"
  ```
  * We are sending requiest to the url and taking the response
  ```py
  response = requests.get(url)
  response
  <Response [200]>
  ```
  *   To display all the text we use ```.text``` This will show all html data
  ```py
  response.text
  ```
  *   Now we need an HTML parser for extracting and formatting HTML Data from webpage therefore we need to install the parser ```lxml```
  ```
  !pip3 install lxml
  ```
  *   Now we will use bsf, response and the parser to store web parsed data in a variable
  ```py
  soup = bsf(response.text,"lxml")
  ```
  ## Now its time for examples
  *   To print all the Anchor tags we will use
  ```py
  for Alink in soup.find_all('a'):
      print(Alink)
  ```
  *   Now if we need to get the content of an attribute Since this is used when we need content of an attribute not the content of an tag.
  ```py
  for Alink in soup.find_all('a'):
      print(Alink.get('href'))
  ```
  *   Now if we need to get the data inside a tag for example extracting data from a ```p``` tag.
  *   To extract only text from a tag we will use ```.text``` function to extract
  ```py
  for ptag in soup.find_all('p'):
      print(ptag.text)
  ```
  *   If we need to extract the headings only from a Paragraph with a bold tag then we will use nested loop for this.
  *   To extract only text from a tag we will use ```.text``` function to extract
  ```py
  for ptag in soup.find_all('p'):
      for btag in ptag.find_all('b'):
          print(btag.text)
  ```
  ## Creating DataFrames with lists
  *   We can create DataFrames by some methods.
      *   CSV, JSON, Excel
      *   Using another DataFrame
      *   Using URL
      *   Using Manually by Lists
  *   Create a list in the form of rows as data and then use ```pd.DataFrame``` to create a DataFrame
  *   Use the keyword ```columns``` to specify the columns name in a list.
  ```py
  akshay = ['Akshay',21,100]
  piyush = ['Piyush',19,50]
  tushar = ['Tushar',25,10]
  colum = ['Name','Age','Marks']
  df=pd.DataFrame([akshay,piyush,tushar],columns=colum)
  ```

  ## API (Application Programming Interface)
  *   It is a medium which establish a connection between client and server to process request and transport data.
  *   Use Case: We use API everyday in many forms like weather API, Database, Twitter API.
  *   There are 4 parameters we need to communicate to an API
      *   consumerkey
      *   consumer_secret
      *   accessToken
      *   accessTokenSecret
  *   So today we will be learning about twitter API.
  *  To use Twitter API we need to install tweepy
  ```
  !pip3 install tweepy
  ```
  *   This function OAuthHandler is used to establish connection between the program and Twitter API.
  ```py
  auth=tweepy.OAuthHandler(consumerkey=consumerKey,consumer_secret=consumer_secret)
  ```
  *   This is used to set the access token
  ```py
  auth.set_access_token("accessToken", "accessTokenSecret")
  ```
  *   Now set the authentication to tweepy for getting access to API
  ```py
  api = tweepy.API(auth)
  ```
  *   Get the Data as search terms from users and the number of words you need.
  ```py
  search = input("Enter word to be search: ")
  numberofwords = int(input("Number of words: "))
  ```
  *   Use the function Cursor to search for the data using API
  ```py
  results = tweepy.Cursor(api.search,q=search).items(numberofwords)
  ```

  ## Text Sentimental Analysis
  *  Sentimental Analysis results two values -1 or +1 if the value is -1 then it is said as negative and if its +1 then it is positive.
  *   Sentimental Analysis can be applied to twitter posts and get the average sentiment state of a HashTag or search item.
  *   To do Sentimental Analysis we need a liberary called ```TextBlob``` and we can install it via.
  ```
  !pip3 install textblob
  ```
  *   Now lets import textBlob
  ```py
  from textblob import TextBlob
  ```
  *   Task is to find sentimental analysis of 10 tweets of a single search term and store the sentiments in a list and calculate average of sentiments to get the rating of a string and display it to users.

  ## Task
  *   Extract data from a webpage
  *   Create Pandas Dataframe of words
  *   Then use Matplotlib to count number of words and plot a bar graph.
  * 3 rows DataFrame with Name, Age, Marks with three people details
  ```py
  akshay = ['Akshay',21,100]
  piyush = ['Piyush',19,50]
  tushar = ['Tushar',25,10]
  colum = ['Name','Age','Marks']
  df=pd.DataFrame([akshay,piyush,tushar],columns=colum)
  df
  ```
  *   Numpy random data to add multiple rows in the previous question.
  *   Task is to find sentimental analysis of 10 tweets of a single search term and store the sentiments in a list and calculate average of sentiments to get the rating of a string and display it to users.
