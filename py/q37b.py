#!/usr/bin/env python
# coding: utf-8

# # Hello welcome

# In[1]:


import numpy as np


# In[2]:


myarr = np.array([3,4,5,6])


# In[3]:


myarr


# In[4]:


print(myarr)


# In[5]:


mua = np.array([3,4,5,6],np.int32)


# In[6]:


mua


# In[7]:


mua[0]


# In[8]:


mj=np.array([[1,2,3],[3,4,5]])


# In[9]:


mj


# In[10]:


print(mj)


# In[11]:


mj[1,2]


# In[12]:


mua.shape


# In[13]:


mj.shape


# In[14]:


mua.dtype


# In[15]:


mj.dtype


# In[16]:


mj[0,1]=90


# In[17]:


mj


# In[18]:


mua[0]=60


# In[19]:


mua


# In[20]:


mua.size


# In[21]:


li = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[22]:


li.size


# In[23]:


mj.size


# In[24]:


k=np.array({1,2,3})


# In[25]:


k.dtype


# In[26]:


zer = np.zeros((2,5))


# In[27]:


zer


# In[28]:


zer.dtype


# In[29]:


np.range(15)


# In[ ]:


sp = np.linspace(1,5,5)


# In[ ]:


sp


# In[ ]:


emp  = np.empty(4,6)


# emp_like=np.empty.like(moj)

# In[31]:


arr = np.identity(45)


# In[32]:


arr


# In[34]:


arr = np.arrange(99)


# In[37]:


mj = mj.reshape(3,2)


# In[38]:


mj


# In[39]:


mj.ravel()


# In[40]:


li


# In[41]:


kp = np.array(li)


# In[42]:


kp.sum(axis=0)


# In[43]:


kp.sum(axis=1)


# In[44]:


kp.T


# In[46]:


kp.ndim


# In[47]:


kp.flat


# In[48]:


for i in kp.flat:
    print(i)


# In[49]:


kp.size


# In[50]:


kp.nbytes


# In[51]:


lol = np.array([4,7,8,9,6])


# In[52]:


lol.argmax()


# In[53]:


lol.argmin()


# In[54]:


lol.min()


# In[55]:


lol.max()


# In[56]:


lol.argsort()


# In[58]:


mj.argmax()


# In[59]:


mj.argmin()


# In[61]:


mj.argsort()


# In[62]:


mj.max()


# In[63]:


mj.min()


# In[64]:


mj.min(axis=0
      )


# In[65]:


mj.max(axis=1)


# In[66]:


mj.argsort(axis=0)


# In[67]:


mj.argmax(axis=0.)


# In[68]:


mj.savel()


# In[69]:


mj


# In[70]:


mj.reshape(6,)


# In[71]:


ar1 = np.array([[4,7,8],[7,9,8],[5,3,8]])
ar2 = np.array([[2,5,4],[8,9,4],[7,2,3]])
prod = ar1*ar2
sum = ar1+ar2


# In[72]:


prod


# In[73]:


sum


# In[74]:


np.sqrt(ar2)


# In[75]:


np.where(ar2>5)


# In[77]:


np.count_nonzero(ar)


# In[78]:


np.nonzero(ar2)


# In[79]:


import sys


# In[80]:


ch = [0,1,2,3,4]
sys.getsizeof(1)*len(ch)


# In[83]:


l = np.array([0,1,2,3,4])
sys.getsizeof(1)*len(l)


# In[ ]:




