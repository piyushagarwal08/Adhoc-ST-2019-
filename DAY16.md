# DAY 16

* Check the tasks details and recheck and do it properly
```
blu 751
home2 600
public_html group apache 2771  set UID
## Linux Commands
  * $ useradd -b /home2  # creates a user with home directory /home2
```
## Notes
  * at real time CPU and RAM can not be changed dynamically without closing the system
  * while launching instance you can add the details to be run at configure instance advanced section as bash commands and it will be run while starting the instance
  * Load Balancer - > distributes the traffic at different urls to be able to handle the traffic
  * On AWS load balancer is called as Elastic load balancer

## Elastic Load Balancer in AWS Cloud
  * From AWS we can use load balancer
  * create Load Balancer
  * they are of 3 types
    1. Classic (for all traffic )
    2. Network
    3. Application
  * Using Classic
  * Define load balancer name
  * Create new security group for ELB
  * configur health check ( most important setting of load balancer )
  * to check if a website is working properly, load balancer pings the ip of your website with http protocol to find index.html
  * Response Time out - > the timeout time in which the response is expected  
  * interval - > after how much time ELB pings to website index page
  * Unhealthy Threshhold - > how many times ELB will try to connect with index if he got no response
  * healthy Threshhold - > checks for no of times to check that your page is working
  * *** ITS NOT FREE ***
  * it checks for running instance to provide you working status
  * using its DNS testing ip

## Machine Learning DAY2
  * using matplotlib.pyplot
  * plotting graphs
    1. plot - > draw lines
    2. bar - > draw bar graphs
    3. pie - > draws a pie chart # plt.pie(data,label=whose data)
  * http://slashlinuxcode.blogspot.com/  - > use this to refer for matplotlib.
  * Main things to focus on are :
    1. pie
    2. bar
    3. scatter
  * official website of matplotlib is https://matplotlib.org
  * Various types of format available in pandas are
    1. CSV
    2. XLS
    3. TEXT
    4. JSON
    5. SQL
  * https://archive.ics.uci.edu/ml/datasets.php - > website used for collecting data set for ML processes
  * Kaggle is also used for same purpose

  ### Categories of ML
    1. Supervised
    2. Unsupervised
    3. Reinforcement

    ### Supervised ML
     * Machine is trained by providing it with various datasets and after training use the machine to test for non-given datas

    ### Unsupervised ML
     * Categorising of data based on homogenous characteristics of the data is done in this category

    ### Reinforcement ML
     * Mostly used in Game autom
