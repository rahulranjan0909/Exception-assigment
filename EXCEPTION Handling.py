#!/usr/bin/env python
# coding: utf-8

# In[1]:


def compute():
    try:
        c=5/0
    except:
        print('Error')
        
compute()


# In[3]:


subjects=["Americans ","Indians"] 
verbs=["play","watch"] 
objects=["Baseball","Cricket"]

for x in range(0,len(subjects)):
    for y in range(0,len(verbs)):
        for z in range(0,len(objects)):
            print(subjects[x]+" "+verbs[y]+" "+ objects[z]+".")


# In[ ]:




