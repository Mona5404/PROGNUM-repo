#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Magnitude inputs
apparentMagnitude = float(input("Apparent Magnitude:"))
absoluteMagnitude = float(input("Absolute Magnitude:"))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

print(f"The distance in parsecs given the magnitudes is {d}")


# In[ ]:




