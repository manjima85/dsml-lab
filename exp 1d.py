#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.Series([10, 20, 30, 40, 50, 60, 70])
data


# In[3]:


data = pd.Series([10, 20, 30, 40, 50, 60, 80], index = ['a','b','c','d','e','f','g'], dtype = 'int8')
data


# In[4]:


data.values


# In[5]:


array_data = data.values

print(array_data)


# In[6]:


data.index


# In[8]:


data_series = {
                'Column1' :  pd.Series([100, 200, 300, 400, 500, 600, 700], dtype = 'int16'),
                'Column2' :  pd.Series([10, 20, 30, 40, 50, 60, 70], dtype = 'int16')
              }
data_series


# In[9]:


pd.DataFrame(data_series)


# In[11]:


movies_df = pd.read_csv('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/boston_train.csv', sep = ',')
movies_df


# In[12]:


movies_df.head()


# In[13]:


movies_df.tail()


# In[15]:


stock_data = pd.read_excel("https://github.com/ammishra08/MachineLearning/raw/master/Datasets/data_akbilgic.xlsx", header=1)
stock_data


# In[16]:


movies_df.shape


# In[17]:


movies_df.columns


# In[18]:


len(movies_df.columns)


# In[19]:


print(movies_df.shape[0], movies_df.shape[1])


# In[20]:


data_series = {
                'Column1' :  pd.Series([100, 200, 300, 400, 500, 600], index = ['a','b','c','d','e','f'], dtype = 'int16'),
                'Column2' :  pd.Series([10, 20, 30, 40, 50, 70], index = ['a','b','c','d','e','g'], dtype = 'int16')
              }
df = pd.DataFrame(data_series)
df


# In[21]:


df.isnull()


# In[22]:


df.isnull().sum()


# In[23]:


df.isna().sum()


# In[24]:


df.notnull()


# In[25]:


df[df['Column1'].isnull() == True]


# In[26]:


df[df['Column2'].isnull() == True]


# In[ ]:




