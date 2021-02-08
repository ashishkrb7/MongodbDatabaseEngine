 
                  ##         #        #                        ###             #
                  # #   #   ###   #   ##    #    ##   ##       #    ##    ##       ##    ##
                  # #  # #   #   # #  # #  # #  ##   ###       ##   # #  # #   #   # #  ###
                  # #  # #   #   # #  # #  # #   ##  #         #    # #   ##   #   # #  #
                  ##    ##   #    ##  ##    ##  ##    ##       ###  # #    #   #   # #   ##
                                                                         ##

# Instruction
This package is for creating the mongodb database and ith various collection dynamically. This can be used standalone or with integrated on API

# Pre-requisites
-  [Mongodb](https://www.mongodb.com/try/download/community) installed on pc
-  [python 3.7.3](https://www.python.org/downloads/release/python-373/) with pip or above

# Folder architecture

      C:.
      │   License
      │   README.md
      │   requirements.txt
      │   setup.sh
      │   __init__.py
      │
      ├───conf
      │       soft.conf
      │
      └───db
              config.json

# How to use it?

> use case 1
```python
from MongodbDatabaseEngine import engine 
engine()
```
It will create the Mongodb database with name mentioned on [soft.conf](https://github.com/ashishcssom/MongodbDatabaseEngine/blob/main/conf/soft.conf) file and create the collection with the name and data available on [config.json](https://github.com/ashishcssom/MongodbDatabaseEngine/blob/main/db/config.json).

> use case 2
```python
from MongodbDatabaseEngine import engine 
engine(databasename="mydatabase")
```
This will create database with name "mydatabase" and utilize the default data mentioned on [config.json](https://github.com/ashishcssom/MongodbDatabaseEngine/blob/main/db/config.json)

> use case 3
```python
import json
userdata=json.load(open(path+r"/db/config.json",'r'))
from MongodbDatabaseEngine import engine 
engine(userdata=userdata, databasename="mydatabase")
```
This use case is for custom database and custom collection data

# Information on config.json | userdata
**engine** methods takes dictionary as input. *Key names* are used as *collection names* and *value* is used as *json array data* user want to store in respective collection.

# Author
   Ashish Kumar
# License
[MIT License](https://github.com/ashishcssom/MongodbDatabaseEngine/blob/main/LICENSE)

# Contributors

<a href="https://github.com/ashishkrb7/MongodbDatabaseEngine/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ashishkrb7/MongodbDatabaseEngine" />
</a>
