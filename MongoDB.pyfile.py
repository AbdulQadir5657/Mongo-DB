#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://qadirabdul5657:Abdul123@cluster0.navxtnr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# In[4]:


get_ipython().system('pip install pymongo')


# In[7]:


# mydatabase
mydb=client["database"]


# In[4]:


client.list_database_names()


# In[8]:


mycol=mydb["myfirstcollection"]


# In[10]:


myfirstrecord={"firstname":"Abdul","lastname":"Qadir","Address":"New Delhi"}


# In[11]:


myfirstrecord


# In[12]:


mycol.insert_one(myfirstrecord)


# In[13]:


mysecondrecord={"firstname":"Abdul1","lastname":"Qadir1","Address":"Old Delhi"}


# In[14]:


mycol.insert_one(mysecondrecord)


# In[15]:


mythirdrecord={"firstname":"Abdul1","lastname":"Qadir1","Address":"Old Delhi","Salary":100000}


# In[16]:


mycol.insert_one(mythirdrecord)


# In[35]:


mutiplerecords=[
    
    {"firstname":"Abdul1","lastname":"Qadir1","Address":"Old Delhi","Salary":100000},
    {"firstname":"mohd","lastname":"saddam","Address":"Delhi","Salary":200000},
    {"firstname":"md","lastname":"Aquib","Address":"New Delhi","Salary":1000000},
    {"firstname":"Faisal","lastname":"Jalees","Address":"south Delhi","Salary":300000}
]


# In[36]:


x=mycol.insert_many(mutiplerecords)


# In[37]:


x.inserted_ids


# In[55]:


mutiplerecords=[
    
    {"_id":1,"firstname":"saquib","lastname":"mohd","Address":"Jharkhand","Salary":56000},
    {"_id":2,"firstname":"shumail","lastname":"ahamad","Address":"Rajisthan","Salary":20000},
]


# In[58]:


mycol.insert_many(mutiplerecords)


# In[59]:


mycol.find_one()


# In[60]:


for x in mycol.find():
    print(x)


# In[69]:


mycol.find_one({"firstname":"md"})


# In[70]:


for x in mycol.find({"Address":"New Delhi"}):
    print(x)


# In[75]:


for x in mycol.find().sort("firstname"):
    print(x)


# In[77]:


for x in mycol.find().sort("firstname",-1):
    print(x)


# In[78]:


mycol.delete_one({"firstname":"Abdul1"})


# In[79]:


for x in mycol.find().sort("firstname",-1):
    print(x)


# In[81]:


for x in mycol.find().limit(5):
    print(x)


# In[82]:


myquery={"firstname":"Abdul"}
newvalue={"$set":{"firstname":"Mohd"}}


# In[83]:


mycol.update_one(myquery,newvalue)


# In[84]:


for x in mycol.find():
    print(x)


# In[85]:


mycol.update_one({"lastname":"Qadir"},{"$set":{"lastname":"Arbaz"}})


# In[86]:


for x in mycol.find():
    print(x)


# In[90]:


# Greater Than

for x in mycol.find({"Salary":{"$gt":100000}}):
    print(x)


# In[91]:


# less than

for x in mycol.find({"Salary":{"$lt":100000}}):
    print(x)


# In[92]:


get_ipython().system(' pip install pandas')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




