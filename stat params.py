#!/usr/bin/env python
# coding: utf-8

# In[2]:


def mean_value(*x):
    y = sum(x)/len(x)
    return(y)
mean_value(4,5,6)

    
    


# In[22]:


def mode(l):
    s = set(l)
    d ={}
    for x in s:
        d[x] = l.count(x)
    return(max(d.keys()))


# In[23]:


l = [4,6,6]
mode(l)


# In[16]:


def mode_value(L):
    s = set(L)
    d = {}
    for x in s:
        d[x]= l.count(x)
    m = max(d.values())
    for k in d.keys():
        if d[k]== m:
            return k
    


# In[17]:


L = [5,6,7,6,5,5,]
mode_value(L)


# In[ ]:




