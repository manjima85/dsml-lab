#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=5
b=11.5
c=1+2j
print(a) 
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))


# In[11]:


s='hello good'
s1='world'
print(s)
print(s[0])
print(s[2:5])
print(s[2:])
print(s * 2)
print(s + s1)


# In[12]:


b=True
print(b)
print(type(b))


# In[13]:


list=['a','b',1,1.5,True]
print(list)


# In[14]:


list=['a','b',1,1.5,True]
print(list)
print(list[0])


# In[15]:


list=['a','b',1,1.5,True]
list1=[2,3,'c',False]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(list + list1)


# In[16]:


a=10>9
print(a)
print(type(a))


# In[1]:


tup= ('a','b','c','d','e')
print("complete tuple=",tup)


# In[2]:


tup= ('a','b','c','d','e')
tup1= (1,2,3,4)
print("complete tuple=",tup)
print("first element=",tup[0])
print("2nd till 3rd=",tup[1:3])
print("starting from 3rd=",tup[2:])
print("tuple 2 times=",tup * 2)
print("concatenated tuple=",tup + tup1)


# In[8]:


dict= {
    "one":"sayu",
    "two":"amna",
    "three":"remna"
     }
print("complete dictionary",dict)
print("perticular key",dict["one"])
print("2nd key",dict["two"])
print(dict.keys())
print(dict.values())


# In[10]:


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("addition:",a+b)
print("substraction:",a-b)
print("multiplication:",a*b)
print("Division:",a/b)
print("modulus:",a%b)
print("floor division:",a//b)
print("exponent:",a**b)


# In[21]:


s1= 'hello'
s2= "world"
s4= "this is a sample program"
s3=s1+' '+s2
print("concatenated:",s3)
print("length",len(s3))
print("uppercase:",s3.upper())
print("lowercase:",s3.lower())
print("first char to upper:",s3.capitalize())
print("specified value:",s3.find('world'))
print("spliting string:",s4.split(' '))
print("replace:",s1.replace('l','m'))


# In[23]:


p=5 > 2
q=-1 < -12
print("AND:",p and q)
print("OR:",p or q)
print("NOT:",not q)


# In[24]:


n=int(input("Enter any number:"))
if(n % 2)==0:
    print(n,"is even")
else:
    print(n,"is odd")
    


# In[26]:


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a >= b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
     largest=c
        
print("Largest of 3 number:",largest)


# In[34]:


n=int(input("enter the num :"))
for i in range(1,num+1):
    print(i)


# In[ ]:





# In[ ]:




