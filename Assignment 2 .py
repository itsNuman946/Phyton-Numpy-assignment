#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[15]:


arr=np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
arr


# In[19]:


newarry=np.reshape(arr,(2,5))


# In[14]:


newarry


# # How to stack two arrays vertically?
# 

# In[22]:


arr=np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
arr


# In[23]:


np.vstack(arr)


# In[24]:


np.hstack(arr)


# # How to convert an array of arrays into a flat 1d array?

# In[28]:


arr=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr


# In[35]:


arr.flatten() 


# # How to Convert higher dimension into one dimension?
# 

# In[36]:


arr=np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
arr.flatten()


# # Convert one dimension to higher dimension?

# In[30]:


arr=np.array([[ 0, 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 9, 10, 11], [12, 13, 14]])
arr


# In[34]:


newar=np.reshape(arr,(5,3))
newar


# # Create 5x5 an array and find the square of an array?

# In[40]:


import numpy as np
x=np.random.randn(5,5)


# In[41]:


np.square(x)


# # Create 5x6 an array and find the mean?
# 

# In[45]:


x=np.random.randn(5,6)
x


# In[43]:


y= x.mean()


# In[44]:


y


# # Find the standard deviation of the previous array in Q8?
# 

# In[46]:


x=np.random.randn(5,6)
np.std(x)


# # Find the median of the previous array in Q8?

# In[47]:


x=np.random.randn(5,6)
np.median(x)


# # Find the transpose of the previous array in Q8?

# In[48]:


x=np.random.randn(5,6)
np.transpose(x)


# # Create a 4x4 an array and find the sum of diagonal elements?

# In[53]:


n=np.arange(1,17).reshape(4,4)
n


# In[54]:


np.trace(n) 


# In[ ]:




