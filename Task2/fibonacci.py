#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2.21 (Session quiz) 
import math

#Start the fib sequence with the first 2 terms 
x = [1,2]
#Loop adding terms
while len(x)<=99:#Only runs until 100th term
    term = x[-1] + x[-2]
    x.append(term)

#Make it into a set (to make it easier to print)
fib = x

print(f"{fib}")


# In[ ]:




