#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()


# In[4]:


x = [5,6,7]
y = [7,9,6]
plt.plot(x,y)
plt.title('Hur')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[6]:


from matplotlib import pyplot as plt
from matplotlib import style


# In[9]:


style.use('ggplot')
x = [5,6,7]
y = [7,9,6]
plt.plot(x,y,'c',label='line',linewidth = 5)
plt.title('Hur')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.grid(True,color = 'k')
plt.show()


# In[5]:


from matplotlib import pyplot as plt
plt.bar([1,3,4,5],[5,2,7,8],label = 'Example One')
plt.bar([2,6,7,4],[4,6,3,9],label = 'Example Two')
plt.legend()
plt.title('Hang')
plt.xlabel('Sell')
plt.ylabel('Taxes')
plt.show()


# In[ ]:





# In[ ]:




