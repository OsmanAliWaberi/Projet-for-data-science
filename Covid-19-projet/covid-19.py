#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/AleynaKocaman/VeriBilimiProjeleri/main/covid19Proje/covid_19_clean_complete.csv')


# In[6]:


data.head(10)


# In[7]:


data.tail(10)


# In[9]:


data.shape


# In[10]:


data.info()


# In[11]:


data.describe()


# In[12]:


data.isnull().sum()


# In[13]:


data.notnull().sum()


# In[17]:


data['Country/Region'].unique()


# In[20]:


data.loc[data['Country/Region']=='Afghanistan',:]


# In[21]:


data.loc[data['Country/Region']=='Afghanistan','Province/State'].isnull().sum()


# In[42]:


data.iloc[:,[0,1]]


# In[74]:


data2 = data.groupby('Country/Region').agg({'Lat':'count'})


# In[90]:


data2.max()


# In[92]:


data2.loc[data2['Lat']==4917,:]


# In[149]:


deaths_sum = data.groupby('Country/Region').agg({'Deaths':'sum'})
deaths_sum['Deaths'].index
    


# In[155]:


plt.figure(figsize=(500,200))
plt.bar(deaths_sum['Deaths'].index,deaths_sum['Deaths'].values)
plt.xlabel('sum for Deaths')
plt.ylabel('Country')
plt.title('The sum of dead people')
plt.show()


# In[ ]:




