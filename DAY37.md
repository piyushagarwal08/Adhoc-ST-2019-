# DAY 37
# SELENIUM

## Installation
* run the following command to install the selenium modules
    ```
    pip install selenium
    ```
* install the chrome webdriver using the following commands,
    ```shell       
    $ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
    $ unzip chromedriver_linux64.zip
    $ sudo mv chromedriver /usr/bin/chromedriver
    $ sudo chown root:root /usr/bin/chromedriver
    $ sudo chmod +x /usr/bin/chromedriver
    ```
## Initialising
* the browser is used in the form of driver
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    # executable path is the location of the chromedriver 
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    ```
* To open any url inside your browser
    ```python
    driver.get("https://www.google.com")
    ```
* To print the title of webpage
    ```python
    print(driver.title)
    ```
* Certain common information that can be easily collected using selenium about web-page are
    ```python
    print(driver.current_url)  # prints the current url of page 

    print(driver.page_source)  # prints the HTML code of the opened web-page
    ```
* To Click on certain link inside the webpage, we use ```x-path``` of the specific link
* To find the ```x-path``` ,
    1. right click on link and open ```inspect element```
    2. right click on the highlighted code and copy the ```Copy XPath```
* use following code to click on link
    ```python
    driver.find_element_by_xpath("enter the copied path").click()
    ```

* To close the tab , opened initially using  ```driver.get``` command, we use ```driver.close()```
* To close all the opened tabs, use ```driver.quit()``` command, instead of ```driver.close()``` inside the python code.

* To use navigate options, forward or backword, run the following command
    ```python
    driver.back()  # move single page backward
    driver.forward() # move single page forward
    ```

## Conditional Commands
* To check if certain fields or images are present on webpage, that is if we can enter in some text fields or if some part of webpage is opened or not, we use the following functions 
    1. is_displayed()
    2. is_enabled()
    3. is_selected()
* To select some field or input element present in the opened webpage
    1. open the inspect element of the specific field
    2. copy the name of the input field
    3. to find the specific field in the automated browser just use the function
        ```find_element_by_name```
    4. Example for the following code
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 

    # creates automated browser
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    # opens the input url
    driver.get("http://www.google.com")
    # creates an instance of the field by name 'q'
    search_field = driver.find_element_by_name("q")
    # if field is displayed
    if search_field.is_displayed():
        # type in the following text inside the text field
        search_field.send_keys("Python")

    driver.close()
    ```
* To check if some ```Radio button``` is selected or not
    1. inspect element of the radio button
    2. copy the value of the button
    3. use the following code
        ```python
        radio_button = driver.find_element_by_css_selector("input[value=name-given-in-value-of-input-field]")
        ```
    4. above code will create an instance of radio button
    5. To check if its selected or or not, just use ```radio_button.isselected()``` function

## Wait Commands
### Implicit Wait Command
* To wait for sometime for all the elements of the page to load properly, we can use ```driver.implicitly_wait(amount-of-time-to-wait-for-in-seconds)```
* the above function, is defined only once and is applicable for all the elements
* ```implicitly_wait``` function will wait for the specific amount of time for all the elements when the load and doesn't move forward with code
* Thus this prevents the synchronisation problem

### Explicit Wait Command
* It is used to define the wait condition for some specific element instead of whole present in the code </br>
*** to be continued ***