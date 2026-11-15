NOTE:
I separated the file for the commit 2-3

Lab Overview:
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