#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def read_csv_from_url(url):
    df = pd.read_csv(url)
    return df


# In[3]:


def test_create_dataframe(dataFrame,list_of_col):
    temp = list(dataFrame)
    
    for i in range(len(temp)):
        if temp[i] not in list_of_col:
            return False
        
    if len(dataFrame) < 10:
        return False
    
    for i in range(len(temp)):
        prev_type = type(dataFrame[temp[i]][0])
        for j in range(1,len(dataFrame)):
                if type(dataFrame[temp[i]][j]) != prev_type:
                    return False
                prev_type = type(dataFrame[temp[i]][j])
                
    return True


# In[ ]:




