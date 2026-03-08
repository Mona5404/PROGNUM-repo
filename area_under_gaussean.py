#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

#Define the Gaussean function
def gauss(x, A, x0, sigma, z0):
    return A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) + z0


#Get input parameters, or default to given values if nothing is entered
print("Gaussian: f(x) = A * exp(-(x-x0)^2/(2*sigma^2)) + z0")
print("Press Enter for defaults: A=1, x0=0, sig=2, z0=0")
A = float(input("A [1.0]: ") or "1.0")
x0 = float(input("x0 [0.0]: ") or "0.0")
sig = float(input("sig [2.0]: ") or "2.0")
z0 = float(input("z0 [0.0]: ") or "0.0")
a_lim = float(input("Integration limit a [0]: ") or "0")
b_lim = float(input("Integration limit b [2.5]: ") or "2.5")

#Plot between -10 and 10 with 200 samples
x_plot = np.linspace(-10, 10, 200)
y_plot = gauss(x_plot, A, x0, sig, z0)

#Plot
fig, ax = plt.subplots()
ax.plot(x_plot, y_plot, "b-", linewidth=2, label="Gaussian")

#Area between a and b using quad, and fill_between
area, err = scipy.integrate.quad(lambda x: gauss(x, A, x0, sig, z0), a_lim, b_lim)

#Mask for fill_between: only within plot range
mask = (x_plot >= a_lim) & (x_plot <= b_lim)
x_fill = x_plot[mask]
y_fill = gauss(x_fill, A, x0, sig, z0)
ax.fill_between(x_fill, y_fill, alpha=0.3, label=f"Area = {area:.6f}")

#Plot 
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Gaussian curve and integration area")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

#Area from -inf to +inf and integral formula for when z0=0 (as when z0=0, the integral is finite)
integ = A * sig * np.sqrt(2 * np.pi)
if z0 == 0:
    area_inf, _ = quad(lambda x: gauss(x, A, x0, sig, z0), -np.inf, np.inf) #Calculates the integral (thus the area) 
    print(f"Area from -inf to +inf (quad): {area_inf:.6f}")
    print(f"Theoretical area A*sigma*sqrt(2*pi): {integ:.6f}")
    print(f"quad() matches theoretical: {np.isclose(area_inf, integ)}")
else:
    print(f"(z0 != 0: skipping -inf to +inf check; total area would diverge)") #Integral is not possible to calculate
    print(f"Theoretical area of Gaussian kernel A*sigma*sqrt(2*pi): {integ:.6f}")

