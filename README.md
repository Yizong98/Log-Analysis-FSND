# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## About
This project is about analyzing backend data through the connection to the database.
Questions to answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
* Python 2 [https://www.python.org/downloads/]
* Vagrant [https://www.vagrantup.com/]
* VirtualBox 3 [https://www.virtualbox.org/wiki/Download_Old_Builds_5_1]
* Environment [https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip]
* Database [https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]

Usage Manual
-------------
* To run, go the folder with logdb.py
* set up vagrant with command: vagrant up
* then use the command: vagrant ssh
* use terminal: python logdb.py in the residing folder. 
* To load the data, cd into the vagrant directory and use the command: psql -d news -f newsdata.sql


