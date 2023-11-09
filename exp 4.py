#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree
from sklearn import tree


# In[3]:


data=load_iris()
x=data.data
y=data.target
print(x.shape,y.shape)


# In[6]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)


# In[7]:


y_pred=dtc.predict(x_test)


# In[8]:


cm=confusion_matrix(y_test,y_pred)
print("confusion matrix:")
print(cm)
print("Classification report - /n",classification_report(y_test,y_pred))


# In[9]:


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4,4),dpi=200)
tree.plot_tree(dtc, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()
fig.savefig("iris_tree.png")


# In[10]:


new_data = [[5.1,3.5,1.4,0.2],[6.2,3.4,5.4,2.3]]
predictions=dtc.predict(new_data)
for prediction in predictions:
    print(f"predicted class: {prediction}")


# In[ ]:




