# %% Import dependencies
import os
import json
import sys
import configparser
from pymongo import MongoClient
from datetime import datetime
#%% Get package path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "./.")).replace("\\","/")
# %% Import configuration files
config = configparser.RawConfigParser()
config.read(path+r'/conf/soft.conf')
config_dict = dict(config.items('Software_configuration'))
# %% MongoDB initialization
def engine(user_data=None,databasename=None):
    """
    To store the data in mongodb
    """
    try:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Upload time
        if user_data==None:
            user_data=json.load(open(path+r"/db/config.json",'r'))[0] # User data
        client = MongoClient(config_dict["mongodb"]) # MongoDB connection string
        if databasename==None:
            mng_db = client[config_dict["databasename"]]  # Database name from config file
        else:
            mng_db = client[databasename]  # Database name from user
        Master_collection_name = mng_db[config_dict["master_collection_name"]] # Master collection
        master_data_json = {"UploadTime": now} # Master data
        masterId = Master_collection_name.insert_one(master_data_json).inserted_id # Create Master collection
        slave_collection=list(user_data)
        f={}
        for _,value in enumerate(list(slave_collection)):
            user_data[value][0].update({"masterId": masterId})
            f[value] = mng_db[value].insert_many(user_data[value])
        return {"message":"Success"}
    except:
        print("Oops! " + str(sys.exc_info()) + " occured.")
        return {"message":"Error"}
# %%
# engine(databasename="alpha")
# %%
