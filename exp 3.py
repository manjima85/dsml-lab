#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split
import sklearn.naive_bayes
dataset = pd.read_csv('Iris.csv')
print(dataset.describe())
print(dataset.head())


# In[2]:


x = dataset.iloc[:,[1,2,3,4]].values
y = dataset.iloc[:,-1].values


# In[3]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[5]:


sc = StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
classifier = sklearn.naive_bayes.GaussianNB()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
ac = accuracy_score(y_test,y_pred)
print("confusion matrix:")
print(cm)
print("Accuracy score:",ac*100,'%')


# In[6]:


new_data = [[5.1,3.5,1.4,0.2],[6.2,3.4,5.4,2.3]]


# In[7]:


predictions = classifier.predict(new_data)


# In[8]:


for prediction in predictions:
    print(f"predicted class: {prediction}")


# In[ ]:




