#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x = np.array([1,2,3,4])
print(x)
print(type(x))
print(x.shape)


# In[2]:


y = np.array([[1,2],[3,4]])
print(y)
print(y.shape)


# In[3]:


z = np.array([[1+0.j,2+5.j]])
print(z)
print(z.shape)


# In[4]:


a = np.zeros((2,3))
print(a)
print(a.shape)


# In[8]:


b = np.ones((2,3), dtype=int)
print(b)


# In[9]:


d = np.eye(3)
print(d)


# In[10]:


e = np.arange(10)
print(e)
e=np.arange(12,21)
print(e)
e = np.arange(5,20,3)
print(e)


# In[11]:


f = np.linspace(1,20,7)
print(f)


# In[12]:


g = np.random.random((3,4))
print(g)


# In[13]:


h=np.random.random((3,4))
print(h.reshape(2,2,3))


# In[14]:


x = np.arange(12)
print(x)
print(x[4])
print(x[-1])
x.resize(3,4)
print(x)
print(x[-1,-1])
print(x[2][3])


# In[15]:


y=np.arange(1,26)
print(y)
print(y[:3])
print(y[10:])
print(y[10:15])
print(y[-5:])
print(y[3:-3])
print(y[::3])
print(y.reshape((5,5)))
print(y)
y = y.reshape((5,5))
print(y)
print(y[:3,:3])
print(y[2:-1,1:-1])
print(y[:,:-1])
print(y[:,-1])
print(y[::,::2])
print(y)
print(y[1::2,1::2])


# In[16]:


a = np.arange(1,6)
b = np.arange(6,11)
print(a)
print(b)
print(a+b)
print(a-b)
print(b-a)
print(a**2)


# In[17]:


print(a>3)


# In[19]:


a=np.arange(0,4).reshape((2,2))
b = np.eye(2)
print(a*b)


# In[20]:


print(np.dot(a,b))


# In[21]:


x = np.arange(1,10).reshape(3,3)
print(x)


# In[22]:


print(x.sum())


# In[23]:


print(x.sum(axis=0))


# In[24]:


print(x.sum(axis=1))


# In[25]:


x = np.arange(1,19).reshape(3,3,2)
print(x)


# In[26]:


print(x.sum(axis=1))


# In[28]:


x = np.arange(1,10).reshape(3,3)
print(x)
print(x.max())


# In[29]:


print(x.max(axis=0))


# In[30]:


print(x.transpose())


# In[ ]:




