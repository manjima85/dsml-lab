#!/usr/bin/env python
# coding: utf-8

# In[4]:


weather=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print(weather_encoded)
print(" ")
temp_encoded=le.fit_transform(temp)
print(temp_encoded)
print(" ")
label=le.fit_transform(play)
print(label)


# In[5]:


features=list(zip(weather_encoded,temp_encoded))
print(features)


# In[6]:


from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(features,label)
predicted=model.predict([[0,1]])
print(predicted)


# In[7]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

irisData=load_iris()
x=irisData.data
y=irisData.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)


# In[8]:


y_pred=knn.predict(x_test)
print(y_pred)


# In[9]:


from sklearn.metrics import classification_report , confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[10]:


print(accuracy_score(y_test,y_pred)*100)


# In[11]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dataset=pd.read_csv('diabetes.csv')
print(len(dataset))
print(dataset)


# In[32]:


zero_not_accepted=['Glucose','BloodPressure','SkinThickness','BMI','Insulin']
for column in zero_not_accepted:
    dataset[column]=dataset[column].replace(0,np.NaN)
    mean = int(dataset[column].mean(skipna=True))
    dataset[column]=dataset[column].replace(np.NaN, mean)
print(dataset['Glucose'],dataset['BloodPressure'],dataset['SkinThickness'],dataset['BMI'],dataset['Insulin'])


# In[12]:


x=dataset.iloc[:, 0:8]
y=dataset.iloc[:, 8]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(len(x_train))
print(len(x_test))
print(len(y_train))
print(len(y_test))


# In[13]:


sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)


# In[14]:


import math
math.sqrt(len(y_test))


# In[15]:


classifier=KNeighborsClassifier(n_neighbors=11,metric='euclidean')
classifier.fit(x_train,y_train)


# In[16]:


y_pred=classifier.predict(x_test)
print(y_pred)


# In[17]:


print(accuracy_score(y_test,y_pred)*100,'%')


# In[18]:


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[20]:


new_data = [[140,72,35,0,33.6,0.627,45,1],[120,70,30,1,25.2,0.2,35,0]]
predictions=classifier.predict(new_data)
for prediction in predictions:
    print(f"predicted target: {prediction}")


# In[ ]:




