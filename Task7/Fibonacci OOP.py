#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#6.14

class Fibonacci: #Adapting week 2 fib sequence code
    """Class for calculating Fibonacci sequence"""
    def __init__(self, N, M):
        self.N = N 
        self.M = M
        self.x = [0,1] #Initialise by getting N and M, and creating the first 2 terms of the fib sequence

    def NthTerm(self):
        if (self.N) == 0:
            self.x = []
        elif (self.N) == 1:
            self.x = [0]
        else:
            #Loop adding terms
            while len(self.x) < self.N: #Only runs until Nth term
                term = self.x[-1] + self.x[-2] 
                self.x.append(term)
        return self.x[-1]
    def NthM(self):
        y = []
        while len(self.x) < self.N:
            term = self.x[-1] + self.x[-2]
            self.x.append(term)
        for i in self.x:
            if (i) % self.M == 0: #Checks if i is divisible by M by returning the remainder
                y.append(i)
        return y

#Test
N = 100 
M = 7

fib = Fibonacci(N,M)
print(f"The example Nth term is {fib.NthTerm()}")
print(f"The example less than Nth term while divisible by M is {fib.NthM()}")

