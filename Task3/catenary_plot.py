#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Session quiz 3.22
import numpy as np
from matplotlib import pyplot as plt

l = list(range(-5,6,1))

#Find the cosh
cosh = np.cosh(l)

#Plot
plt.plot(l, cosh, marker='X', color='pink') #create the plot with x and cosh
plt.title("Plotting a Catenary", fontsize = 12) #Title
plt.ylabel("cosh(x)", fontsize = 10) #Y axis label
plt.xlabel("x", fontsize = 10) #X axis labek
plt.grid()
plt.show()

#Creating an array using arrange
arr = np.arrange(-5, 6, 1)
print(f"The list is {l}, and the array created with arrange is {arr}")

#Run in terminal as .py

