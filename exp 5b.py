#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score


# In[3]:


data_df = pd.read_csv('CCCP - Sheet1.csv')
data_df.head()


# In[4]:


x = data_df.drop(['PE'],axis=1).values
print(x)
y = data_df['PE'].values
print(y)


# In[5]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=0)


# In[6]:


regressor = LinearRegression()


# In[7]:


regressor.fit(x_train,y_train)


# In[8]:


y_pred = regressor.predict(x_test)
print(y_pred)


# In[9]:


plt.figure(figsize=(15,10))
plt.scatter(y_test,y_pred)


# In[10]:


plt.xlabel('Actual')
plt.ylabel('predicted')
plt.title('ACTUAL VS PREDICTED')
plt.show()


# In[11]:


mse = mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)


# In[12]:


mae=mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print("Mean squared error (MSE):", mse)
print("Root Mean squared error (RMSE):", rmse)
print("Mean absolute error (MAE):", mae)
print("R-squared (R2):", r2)


# In[14]:


new_input=[[14.96,41.76,1024.07,73.17]]
y_pred = regressor.predict(new_input)
print("Predicted target values:",y_pred)


# In[ ]:




