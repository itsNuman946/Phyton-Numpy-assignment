#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


invent=pd.read_csv("Assignment_Csv/inventory.csv")


# In[9]:


invent


# In[3]:


invent.head(10)


# In[5]:


product_request=invent[invent['location']== "Staten Island"]


# In[6]:


product_request


# In[10]:


seed_request=invent[(invent['location']=="Brooklyn") &(invent['product_type']=="seeds")]


# In[11]:


seed_request


# In[13]:


invent['in_stock']=invent['quantity']>0


# In[14]:


invent


# In[15]:


invent['total_value']=invent['price']*invent['quantity']


# In[16]:


invent


# In[17]:


combine_lambda = lambda row:'{} - {}'.format(row.product_type, row.product_description)


# In[18]:


combine_lambda


# In[21]:


invent['full_description']=invent.apply(combine_lambda,axis=1)


# In[22]:


invent


# In[ ]:




