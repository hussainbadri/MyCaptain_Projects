#!/usr/bin/env python
# coding: utf-8

# In[12]:


a=int(input('Enter a number upto which you want to print fibbonacci series: '))
if a>0:
    i=0
    x=0
    y=1
    b=[]
    b.append(x)
    b.append(y)
    while i<a-2:
        z=x+y
        b.append(z)
        x=y
        y=z
        i=i+1
    print(b)
else:
    print('Please enter a number greater than zero')


# In[ ]:




