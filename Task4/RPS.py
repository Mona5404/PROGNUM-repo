#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Session quiz 4.3
from numpy.random import randint

#Make the user choose their warrior of choice 
Uc1 = input(f"Choose between Rock(R), Paper(P) or Scissors(S):")
Uc = Uc1.upper()#Make it case insensitive
Cc = randint(1,3+1)#The computer's choice, chooses between 1 to 3 

#Changing the computer's choice from a number to a letter, R, P or S
if Cc == 1:
    Cc = 'R'
elif Cc == 2:
    Cc = 'P'
else:
    Cc = 'S'

#Conditions for win, loss or tie
if Uc == Cc:
    print(f"It's a tie!") #If they are the same, it is a tie
elif Uc == 'R':
    if Cc == 'P':
        print(f"You lose! Hahahahahahahahaha")
    else: 
        print(f"You win :(")
elif Uc == 'P':
    if Cc == 'S':
        print(f"You lose! Hahahahahahahahaha")
    else: 
        print(f"You win :(")
else:
    if Cc == 'R':
        print(f"You lose! Hahahahahahahahaha")
    else: 
        print(f"You win :(")

print(f"The computer chose {Cc}")

