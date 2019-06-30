# DAY 26

## Database
  * MySQL
  * Postgre SQL
  * MSSQL
  * DB2
  * Oracle
  * Aurora
  * Mariadb

## Popular attacks
  * Bash
  * ssh heart bleed
  * SQL injection

## Requirements for DBA
  * Server - > to save data
  * Security - > secure from hackers and sql injections
  * Performance - > easy to write and fetch at high speed
  * If fails how to get data back
  * save from Hacking
  * Migrate from one environment to other
  * SQL Query --> (0.0001 %)

## RDS (Relational Databases Services)
  * It is a collection of all the above DBA requirements provided by AWS services
  * RAM and CPU are allocated dynamically
  * Single tier Architecture web application - > when both website and database are present on single server

```
                              |- - - - - - - - - ^
                              |                  |
[SQL Database] - - - - > [Website] - - - - > [Server]
      ^                        |  
      | - - - - - - - - - - - -          

                    MULTI-TIER ARCHITECTURE
```
  * RDS is the most highest paid service on AWS
  * it is SQL type DB
  ### How to Connect with RDS with EC2
    * Amazon never gives access to RDS
    * Port no of RDS is 3306
    * Data transmission works through socket programming
    * Database Mgration - > migrating data from one server to other
    * Remote SQL - > running SQL queries through different os
    ```
    mysql -u root -h database1.cs4a2twonycl.ap-south-1.rds.amazonaws.com -p
    ```

## NOSQL
  * NOSQL - > no structured query language
  * creates columns on real time
  * DynamoDB - > an NOSQL database , used for <b>PUBG</b> like games

## Pyton with RDS
  * install python module
  ```
  pip3 install mysql-connector-python
  ```
  * connector code
  ```python
  #!/usr/bin/python
  import mysql.connector as mysql
  # RDS information
  username='enter-username'
  password='enter-your-pass'
  database_name='enter-db-name'
  host='enter-end-point-of-db'

  # Now connecting the Database
  conn=mysql.connect(user=username,password=password,database=database_name,host=host)
  # Now generating a SQL language cursor
  cur = conn.cursor()

  # Now we can write SQL query
  #cur.execute('show tables;')

  # Now printing data
  #print(cur.fetchall())

  # closing connection
  conn.close()

  ```

# ML - OPENCV

  * 0xff == ord('keyboard-key') # this is a method in python to make sure program knows a certain key is pressed
