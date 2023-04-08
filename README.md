# oqctest
A circuits management system built using Django framework. It is designed for simulation of rotating quantum bit (Qubit) and calculate the result of its 0 and 1 states.
The features also include operations recording and every single record can be found by id.

## Installation

Python and libraries listed in requirements.txt need to be installed

```bash
pip -r requierments.txt
```


## Usage

Go to the oqctest folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Get Data

The Get Data page is the default page for user.  

The previous records will be displayed as response.

## Add Item

You can access the add item page at **http://127.0.0.1:8000/job** 

A content blank is provided my django framework, you can select Mdedia type = "application/json" and input your circuits into the blank. After clicking "post" button below, your input will be check if the format is correct.

For two types of acceptable input formats, please refer "documents/test-cases.txt"

## Search Single Job

You can access the search single job page at **http://127.0.0.1:8000/job/<int:job_id>** 

Every correct circuit you input will be stored on the server and an unique job_id will be automatically formed in type of auto_increase integer starts from 1.

Example:
**http://127.0.0.1:8000/job/120** refers to find the 120th operation recorded on the server, if there is no such a record an exception will be thrown.


## Screenshots

###Get data page
![get_data.png](https://s2.loli.net/2023/04/08/OsFItJzRM9evySn.png)

###Add item page
![add_item.jpg](https://s2.loli.net/2023/04/08/3MC29I1wKBfOGxr.jpg)

###search single job page
![search_single_job.jpg](https://s2.loli.net/2023/04/08/qW1LhspFv4EbfP9.jpg)
