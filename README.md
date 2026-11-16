NOTE:
I separated the file for the commit 2-3 (filter.py)

Lab Overview - Commit 3:
Well, this lab is all about implementing google sheets filtering and "matrix-style" data to python/coding.

Files:
- README.md
- filter.py
- data_processing.py
- Countries.csv
- Cities.csv

Table - mainly hold data (dict type)
{"city": "Berlin", "country": "Germany", "temperature": "9.5"}

attribute:
- rows

methods:
- filter(self, condition), pick rows to match and return
- aggregate, Takes one column from all rows and runs a math on it

DataLoader - read csv file

As for "how to test and run the code",
Just simply run the desired file.

---------------------------------------------

Lab Overview - Commit 4

This lab is mainly all about OOP, of course, handling file from external place and matching those results

As for the files:
commit-4.py is for, well, commit 4
test.txt is just testing, nothing to be concern about
README.md has been modified to include both commit 3 and 4

DataLoader - load in .csv

DB stores named tables
- tables : for mapping
- insert() saves
- search() search it up

Table hold rows and filtering
- table_name
- rows
- filter() return
- aggregate(x,y) give a whole overview of column
- join() combines rows