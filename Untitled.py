#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import seaborn as sns


df = pd.read_csv("C:\\Users\\SIMRAN\\Downloads\\housing.csv")
df.head()


# In[82]:


df.isnull().sum()


# In[83]:


mean_val = df['total_bedrooms'].mean()
print(mean_val)


# In[84]:


df['total_bedrooms'] = df['total_bedrooms'].fillna(538)


# In[85]:


df.isnull().sum()


# In[86]:


df.head(10)


# In[87]:


df.duplicated()


# In[88]:


df.duplicated().sum()


# In[89]:


sns.boxplot(data=df['total_rooms'])


# In[90]:


df.describe()


# In[91]:


val = df.describe()


# In[92]:


iqr = val['total_rooms'][6]-val['total_rooms'][4]
iqr


# In[93]:


ll = val['total_rooms'][4] -(1.5 * iqr)
ul = val['total_rooms'][6] +(1.5 * iqr)
print(ll,ul)


# In[96]:


df['val'] =df['total_rooms'].apply(lambda x: 'True' if x >= ll and x<=ul else 'False')
df['val']#outliers


# In[ ]:




