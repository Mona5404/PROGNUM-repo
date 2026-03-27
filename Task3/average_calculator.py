#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Session quiz 3.1

#Masses list
masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
moon = 7.349e+22 #Defining the moon mass for convenience

planets = [] #New list

#Creating a planets only list
for M in masses:
    if M <= moon:
        pass
    else:
        planets.append(M)

print(f"The list of objects that are greater than the mass of the moon is {planets}")

#Slice for last 5 of original list
n1 = len(masses)
n = n1 - 5 #Get the length of the masses list, subtract 5 from the number to get our starting point
masses1 = masses[n::1] #Slice the masses list from n to the end, with a step of 1 

print(f"The new list is {masses1}")

#Average mass of new list
s = sum(masses1)
avgm = s/n

print(f"The average mass of the sliced masses list is {avgm}")

#Download as .py and run on terminal 

