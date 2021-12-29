# pydb

Database API wrapper for python

> Tested with .accdb databases

## How to use

Install the package using pip:

` 
  pip install git+https://github.com/Pablo-Valverde/pydb.git
`

Import the package:

```
  import pydb
```

Create a new DBBroker object passing it the database path as an argument:

```
  broker = pydb.DBBroker(PATH_DB)
```
 
 Now the database can be accesed using:
 
 ```
  broker.Read(sql)
  broker.Insert(sql) 
  broker.Delete(sql)
  broker.Update(sql)
 ```
 
 Read returns an iterable with the values asked for in the sql query.
 
 Insert, Delete and Update returns the number of rows affected by the sql query.
