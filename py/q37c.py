#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dict = {
    "name":['hero','king','love','chandu','kappu','raju'],
    "marks":[90,86,97,56,86,99],
    "city":['kolapur','sonpur','bokaro','agra','bihar','delhi']
}


# In[3]:


df = pd.DataFrame(dict)


# In[4]:


df


# In[5]:


df.to_csv('marks.csv')


# In[6]:


df.to_csv('marks_false.csv',index = False)


# In[7]:


df.head()


# In[8]:


df.head(2)


# In[9]:


df.tail(2)


# In[10]:


df.describe()


# In[ ]:





# In[ ]:




