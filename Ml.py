
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('/root/marks.csv')


# In[3]:


type(data)


# In[4]:


data.head()


# In[20]:


x=data["Hour "]


# In[21]:


import numpy as np


# In[22]:


x.shape #the shape of x is 1D which doesn't fit in the model.fit() so we have to convert it first to 2D 
# so we have to reshape it first 
# first convert to numpy array then reshape


# In[23]:


x=x.values # converted to numpy array to be able to reshape


# In[24]:


type(x) #see converted into numpy array


# In[26]:


x=x.reshape(29,1)


# In[27]:


x.shape # now shape is 2D


# In[28]:


y=data["Marks"]


# In[29]:


from sklearn.linear_model import LinearRegression


# In[30]:


model= LinearRegression() #in starting it is empty like new born child 


# In[35]:


model.fit(x,y) # succesfully fitted


# In[36]:


model.coef_


# In[37]:


model.intercept_


# In[43]:
#prediction:
no_of_students=int(input("how many students marks you want to predict : "))
for i in range(no_of_students):
    hour=input("how much hours do you study? :")
    hour_int=float(hour)# to convert it into float type because "input" return string
    type(hour_int)
    marks=model.predict([[hour_int]])# this cmd take only int or float
    marks_final=float(marks)
    print(f"you predicted marks is {marks_final}")






