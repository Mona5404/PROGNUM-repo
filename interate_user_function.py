#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import sin, cos, exp, pi
import numpy as np
from scipy.integrate import quad

#Define the function
def interate_user_function():
    print("We will integrate a function f(x) from 0 to pi. sin, cos, exp, pi, and numpy as np are allowed. E.g.: x**4 + exp(sin(x) + cos(x))")
    expr = input("\nEnter function in x:\n") #Function input

    #Check if f(x) is a valid function, return an error message to the user if not 
    def f(x):
        # x, sin, cos, exp, pi, np are available 
        try:
            return eval(expr)
        except NameError as e:
            print("NameError:", e)
            print("You probably used a name or function that is not defined.")
            print("Use only: x, sin, cos, exp, pi, np.")
            raise
        except SyntaxError as e:
            print("SyntaxError:", e)
            print("Check your expression (parentheses, operators, etc.).")
            raise
        except Exception as e:
            print("Error while evaluating your function:", e)
            raise

    #Integration with quad()
    try:
        result, error = quad(f, 0.0, pi)
        print(f"\nquad(): integral from 0 to pi = {result:.6f} ± {error:.2e})")
    except Exception as e:
        print("\nCould not compute the integral with quad().")
        print("Reason:", e)

    # Monte Carlo integration
    try:
        N = 100000
        a, b = 0.0, pi
        xs = np.random.uniform(a, b, N)
        values = []

        for x in xs:
            values.append(f(x))

        values = np.array(values)
        length = b - a
        mc_result = np.mean(values) * length
        mc_error = np.std(values) * length / np.sqrt(N)

        print(f"\nMonte Carlo: integral from 0 to pi ≈ {mc_result:.6f} ± {mc_error:.2e}")
    except Exception as e:
        print("\nMonte Carlo integration failed.")
        print("Reason:", e)

interate_user_function()

