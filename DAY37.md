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
* Certain methods to find the elements are:
    1. find_element_by_id("enter-specific-id")
    2. find_element_by_xpath("enter-specific-xpath")
    3. find_element(By.ID,"enter-specific-id")
        * to use ```By``` function, we use the following module
            ```from selenium.webdriver.common.by import By```
    4. find_element_by_css_selector("input[value=name-given-in-value-of-input-field]")
    5. find_element(By.XPATH,"enter-specific-xpath")

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
* To clear certain fields/text_fields use the function
    ```driver.find_element_by_id("id").clear()```

## Wait Commands
### Implicit Wait Command
* To wait for sometime for all the elements of the page to load properly, we can use ```driver.implicitly_wait(amount-of-time-to-wait-for-in-seconds)```
* the above function, is defined only once and is applicable for all the elements
* ```implicitly_wait``` function will wait for the specific amount of time for all the elements when the load and doesn't move forward with code
* Thus this prevents the synchronisation problem

### Explicit Wait Command
* It is used to define the wait condition for some specific element instead of whole present in the code 
* requires another module named  ```from selenium.webdriver.support import expected_conditions```
* To make sure the code waits for certain condition to be True,follow the steps
    1. create a instance to define how much time driver has to wait and it is done using module
        ```python
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(driver,time-in-seconds)
        # time here is the max time it will wait for a certain condition to be true, if condition is true before max-time then the code will not wait anymore
        ```

    2. find the ID or Xpath or Value(css-selector)
    3. type the following code
        ```python
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"enter-the specific - xpath"))

## Find how many similar elements Exist
* In websites, the similar elements like input boxes or text fields or buttons have similar class as well and thus we can calculate the no of similar elements in a webpage using class
* The function used to do so is ```find_elements(By.CLASS_NAME,"name-of-class")

## Working with Dropdown list
* To work over dropdown list, the function required is ```Select```, it can be imported as
```python
from selenium.webdriver.support.ui import Select
dropdown_list  = Select(driver.find_element_by_id("id-of-dropdown list"))
```
* To select a option from list
```python
dropdown_list.select_by_visible_text("Specify the text to be selected from options")
```
* To select by Index
```python
dropdown_list.select_by_index(index-position-without-quotes)
```
* To select by Value, since every option in drop down list has different value
```python
dropdown_list.select_by_value("enter the value of the specific option")
```
* To calculate no of options in drop down list use ```len(dropdown_list.options)```
* ```dropdown_list.options``` provides a ```list``` of all the options given in dropdown list
* To find all the available options in a dropdown list, the value of options, use ```dropdown_list.options[0].text```

## Working with links 
* to store or find all the links available in a webpage we use ```TAG_NAME``` function
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

links = driver.find_elements(By.TAG_NAME,"a")
# this will provide a list of all the lists present on webpage
```
* To print the text value from links we just use ```links.text``` for every link stored in ```links list```

* Using the values provides with links in website , we have 2 ways to automate the selection of links
    1. By.LINK_TEXT
    2. By.PARTIAL_LINK_TEXT 
* LINK_TEXT ~> In this we provide the complete exact value of the link
```python
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="thepath")

driver.find_element(By.LINK_TEXT,"REGISTER").click()
#or
driver.find_element_by_link_text("text-in-link")
# or
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
# <a href="http://www.google.com">REGISTER</a>
```

## Alerts
* To work on alert boxes , we need to make sure that our automated browser is being switched to Alert box that we can do using ```driver.switch_to_alert()```
* To Accept a alert box, run command ```driver.switch_to_alert().accept()```
* To reject a alert box, run command ```driver.switch_to_alert().dismiss()```
* To switch to default content, or normal page use function ```driver.switch_to.default_content()```

## Iframes
* The selenium works on page not on frames
* To work on different frames, we need to specify the frame the selenium has to work on available on the page
* To switch frames the function used is ```driver.switch_to.frame("name-of-frame/class-name/frame-id")```
* To switch to default content, or normal page use function ```driver.switch_to.default_content()```

## Window Handles
* The tabs present in a browser of selenium are referred as ```handles```
* To get the value of current working ```window handle```, we use the function ```driver.current_window_handle```
* the value of ```window handle``` is a random generated sequence of ```Alpha~Numerical digits```
* To get a list of all the opened ```tabs``` in selenium ```browser``` we use the function ```driver.window_handles```
* To switch the working window similar to frames we use the function ```driver.switch_to.window('sequence-of-window-handle')```

## Adding Chrome Extensions
* To use certain chrome extension, instead of applying them manually at run time, it's easy to add them before hand using the ```.crx``` file
* To add a extension , first we need the .crx file of the extension and for that~
    1. first open ```https://crxextractor.com/``` and add the url of the specific action
    2. Download the file and move it to path ```/usr/bin``` with ```chromedriver``` and make sure that it is ```executable```
* use this code to add the specific extension in broswer
    ```python
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_extension("path-of-crx-file")
    driver = webdriver.Chrome(options=options)
    ```
* Using above code, the opened browser will be available with  ```specified``` extension by default

## Window Scrolling
* There are 3 basic approaches to scroll down a web - page
    1. ### By Pixel Position
        * To scroll down the web page by certain pixels ,which are calculated by intuition, we can run ```javascript``` format code, that is
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        driver.execute_script("window.scrollBy(0,1000)","")
    
        # driver.execute_script("window.scrollBy(starting-position,ending-position)","")
        ```
        * This is a specific format made to use webpage scrolling

    2. ### Scroll Page till some element is not discovered
        * This method is used to scroll down the page until some specified element is not found
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        element_to_Scroll_to = driver.find_element_by_xpath("xpath-of-that-element")
        driver.execute_script("arguments[0].scrollIntoView();",element_to_Scroll_to)
        
        # this code will make sure that page is scrolled down till the specified xpath is not found over webpage and it is shown on top
        ```
    
    3. ### Scroll down to the end of page
        * This is thing is not necessarily required , but still
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        ```
## Mouse Actions
* Various actions that can be done using mouse are:
    1. Mouse hovering
    2. Right click using mouse
* For use of mouse in automated selenium browser we use the module ```ActionChains```
* It can be imported as ```from selenium.webdriver import ActionChains```
* Way os using mouse actions
    1. To hover over a 3 elements and click on an element, the following code is useful
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    element2 = driver.find_element_by_xpath("xpath-of-element-no-2")
    element3 = driver.find_element_by_xpath("xpath-of-element-no-3")

    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.move_to_element(element1).move_to_element(element2).move_to_element(element3).click().perform()
    # perform defines the final point, to define that all mouse actions are defined

    # the above code will hover mouse over element 1 then move to element 2 location and finally followed by moving to element3 location and will click on it
    ```

    2. To double click on some element , use the ```double_click()``` function
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.double_click(element1).perform() # double click on element
    ```

    3. Right click on any element
    * To perform right click function over any element we use the ```context_click()``` function
    * The following code is used to perform this action using ```ActionChains``` module
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    element1 = driver.find_element_by_xpath("xpath-of-element-no-1")
    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.context_click(element1).perform() # double click on element
    ```

    4. Drag and Drop things using mouse
    * This is not much of a usable function
    * It is used to move an element from one position to another element position
    * For this first find the ```source-position-element``` and ```destination-position-element```
    * Then create ```action``` instance of ```ActionChains(driver)``` function
    * Finally use  ```drag_and_drop``` function for the purpose
    ```python
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    # automated browser is initiated
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

    # Need to make instances of elements need to do mouse actions on
    source_element = driver.find_element_by_xpath("xpath-of-element-no-1")
    destination_element = driver.find_element_by_xpath("xpath-of-element-no-1")    
    # time to create an object of ActionChains for mouse actions
    actions = ActionChains(driver)

    actions.drag_and_drop(source_element,destination_element).perform()
    ```

## Uploading Files
* To upload certain file, we just need to ```find the element``` using ```id/name/xpath```
* Then just use ```send_keys``` method to upload the file by specifying the ```path``` of file need to be uploaded.

## Download Files
* To download any files, just make sure to provide required amount of wait for downloading before closing the browser
* To change the default directory of automated browser
    ```python
    from selenium import webdriver
    from seleium.webdriver.chrome.options import Options

    chrome_options = Options()

    # prefs stands for preferances
    # in the dictionary we can add any number of required changes
    chrome_options.add_experimental_option("prefs",{"download.default_directory": "path-of-download-directoroy"})

    driver = webdriver.Chrome(executable_path="path-of-driver",chrome_options = chrome_options)
    ```
* downloading any file is similar as clicking a download button using ```find element```

## Excel Operations
* For tasks related to ```excel``` file we use another module called ```openpyxl```

### Reading From Excel File
* To read data from some ```Excel File``` we use a function called ```load_workbook```
```python
import openpyxl

workbook = openpyxl.load_workbook("path-of-excel-sheet")

# to get a specific sheet out of workbook
sheet1 = workbook.get_sheet_by_name("Sheet1")

# if there is single sheet, we can just use
sheet = workbook.active

# to find the total no of rows
row=sheet.max_row

# to find the total no columns
column=sheet.max_column

# to read the data from excel value loaded in code
for i in range(1,row+1):  # this loop works for each row,avoiding headers
    for j in range(1,column+1):  # this loop works for each column
        print(sheet.cell(row=i,column=j).value,end="   ")
    print() # this print is used to print a new line character and move to next line
```

 ### Writing to Excel File
 * To write inside a Excel file through python , use similar code
 ```python
 import openpyxl

 workbook = openpyxl.load_workbook("path-of-excel-sheet")

 sheet = workbook.get_sheet_by_name("Name of you sheet")

 for i in range(1,row):
    for j in range(1,column):
        sheet.cell(row=i,column=j).value="whatever-you-want-to-type-in file"

workbook.save("path-of-excel-file")
```

## Cookies
* To get the present cookies of browser, we use ```driver.get_cookies()```
* Cookies are present in ```Dictionary``` format
* To delete all cookies use ```driver.delete_all_cookies()```
* Adding cookies from a file is difficult for now as a file contains string and cookie should be dict 
* for more then one cookie we use list of dictionaries with each dictionary element acting as a single cookie


## Capture ScreenShot



