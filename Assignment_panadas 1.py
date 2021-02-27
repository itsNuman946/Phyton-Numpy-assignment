#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[19]:


a=pd.read_csv("assignment_Csv/states0.csv")
a


# In[20]:


b=pd.read_csv("assignment_Csv/states1.csv")
b


# In[28]:


c=pd.read_csv("assignment_Csv/states2.csv")
c


# In[51]:


d=pd.read_csv("assignment_Csv/states3.csv")
d


# In[52]:


e=pd.read_csv("assignment_Csv/states4.csv")
e


# In[53]:


f=pd.read_csv("assignment_Csv/states5.csv")
f


# In[54]:


g=pd.read_csv("assignment_Csv/states6.csv")
g


# In[55]:


h=pd.read_csv("assignment_Csv/states7.csv")
h


# In[56]:


i=pd.read_csv("assignment_Csv/states8.csv")
i


# In[57]:


j=pd.read_csv("assignment_Csv/states9.csv")
j


# In[58]:


k=pd.read_csv("assignment_Csv/inventory.csv")
k


# In[117]:


frame=[a,b,c,d,e,f,g,h,i,j]


# In[118]:


mergedFrames=pd.concat(frame, sort=True)


# In[119]:


mergedFrames.index=[np.arange(60)]
mergedFrames.drop(columns=["Unnamed: 0"],inplace=True)


# In[120]:


mergedFrames.to_csv("final_output.csv", index=False)


# In[121]:


mergedFrames.dtypes


# In[122]:


mergedFrames


# In[123]:


mergedFrames[['Male','Female']]=mergedFrames.GenderPop.str.split("_",expand=True)


# In[124]:


mergedFrames.drop(columns=['GenderPop'],inplace=True)


# In[125]:


cenus=mergedFrames.reindex(columns=['State','TotalPop','Asian','Black','Hispanic','Income','Native','Pacific','White','Male','Female'])


# In[126]:


cenus


# In[127]:


cenus.head()


# In[128]:


cenus['Income']=cenus.Income.str.strip('$')


# In[130]:


cenus.head()


# In[131]:


cenus=cenus.replace('%','',regex=True)


# In[132]:


cenus.head()


# In[133]:


cenus=cenus.replace('M','',regex=True)


# In[134]:


cenus=cenus.replace('F','',regex=True)


# In[135]:


cenus.loc[:,'Asian':'White']=round(cenus.loc[:,'Asian':'White'].apply(pd.to_numeric),2)


# In[136]:


cenus.head()


# In[138]:


cenus.drop(columns=['Female'],inplace=True)


# In[139]:


cenus.head()


# In[142]:


cenus['Male']=cenus.Male.astype(int)


# In[143]:


cenus['Female']=cenus['TotalPop']-cenus['Male']


# In[144]:


cenus.head()


# In[145]:


cenus.dtypes


# In[153]:


import matplotlib.pyplot as plt
plt.scatter(cenus['Female'],cenus['Income'])
plt.xlabel('Salary $', fontsize=18)
plt.ylabel('Female_Population', fontsize=16)
plt.show()


# In[147]:


cenus.duplicated()


# In[151]:


cenus.drop_duplicates(inplace=True)


# In[152]:


plt.scatter(cenus['Female'],cenus['Income'])
plt.xlabel('Salary $', fontsize=18)
plt.ylabel('Female_Population', fontsize=16)
plt.show()


# In[154]:


Final_cenus= round(cenus.loc[:,'Asian':'White'].apply(lambda x:x*cenus['TotalPop']/100))


# In[155]:


Final_cenus.head()


# In[156]:


Final_cenus.fillna(method='bfill',inplace=True)


# In[157]:


Final_cenus.astype(int)


# In[158]:


Final_cenus.hist(column='White')


# In[160]:


Final_cenus.hist(column='Hispanic')


# In[161]:


Final_cenus.hist(column='Asian')


# In[162]:


Final_cenus.hist(column='Black')


# In[163]:


Final_cenus.hist(column='Native')


# In[164]:


Final_cenus.hist(column='Pacific')


# In[165]:


Final_cenus.hist(column='Income')


# In[ ]:




