#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score


# In[7]:


dataset = pd.read_csv('Salary_data - Salary_data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
print(dataset.head())


# In[8]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)


# In[14]:


regressor = LinearRegression()
regressor.fit(x_train, y_train)


# In[15]:


plt.scatter(x_train,y_train,color='red',label='Actual')
plt.plot(x_train,regressor.predict(x_train),color='blue',label='predicted')
plt.title('salary VS Experience(Training set)')
plt.xlabel('year of Experience')
plt.ylabel('salary')
plt.legend()
plt.show()


# In[16]:


plt.scatter(x_test,y_test,color='red',label='Actual')
plt.plot(x_train,regressor.predict(x_train),color='blue',label='predicted')
plt.title('salary VS Experience(Test set)')
plt.xlabel('year of Experience')
plt.ylabel('salary')
plt.legend()
plt.show()


# In[17]:


y_pred = regressor.predict(x_test)
y_pred


# In[20]:


mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
mae=mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print("Mean squared error (MSE):", mse)
print("Root Mean squared error (RMSE):", rmse)
print("Mean absolute error (MAE):", mae)
print("R-squared (R2):", r2)


# In[21]:


new_input=[[5]]
y_pred = regressor.predict(new_input)
print("Predicted Salary:",y_pred)


# In[ ]:




