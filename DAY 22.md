# DAY 22

## Permissions

  * $ chmod a-rwx file-name # permission for all
  * permissions to a directory can be given either by root or owner of directory
## Task for Non-HTML
  * on ec2, launch a webserver and /var/www/html/AI here store playbooks
  * when each playbook is seen on browser, whatever playbook is clicked, it should run

## Task for HTML
  * Project: Platform as a service for AI
    * ask for name
    * show some options on what to work
      1. pandas
      2. numpy
      3. ML
    * whatever user selects should get an terminal with required service in that
    * option for Data Processing - > dropdown to find missing values or irrelevant data that processes it and gives it back for download


## ML

### SVM ( Support Vector Classifier )
  * in Support Vector Classifier read about kernel and gamma
  * Kernel is a mathematical formula used to high tune the SVM
  * study in which case we are supposed to use the specific kernel

* spam-mail is the mail moves in spam folder
* mails in inbox category are called ham

### Random Forest
  * It is the accurate or advanced version of Decision Tree
  * In this many DecisiomTreeClassifiers are combined to create a single classifier
  * It will choose randomly from the number of end nodes of all the trees with highest accuracy score
  *

### Naive Based Algorithm
  * It is based upon Conditional Probablity
  * It is used by mail-servers to relatively differentiate between spam and ham
  * Creating collection of words from a single word is stem and process by which these words are generated is called stemming
  * Example - :
    goes,gone,going,go >- all are part or have root node as go

 ### SMTP and python
  * SMTP stand Server mail transfer protocol works on TCP(25) protocol
  * module name - > smtplib
  * MUA - > Mail User Agent ,platform where we enter our login credentials to send or recieve mail, software used to read mails  
  * MDA - > Mail Delivery Agent , delivers mail to users
  * MTA - > Mail Transfer Agent , delivers mail to server
  * Secured version of SMTP is SMTPS with protocol 465/513
  * SMTPS - > Secure Mail Transfer Agent
  * we need to make a MUA using python to read and send mails through mail-server
  * Port no of POP3(110) , Port no of IMAP(143)
  * Port no of POPS(995) , Port no of IMAPS(993)
  * need to allow insecure channel
