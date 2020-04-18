
from scipy import exp, sqrt

def lv(state, time, alpha, beta, gamma, delta):
    
    x = state[0]
    y = state[1]
    dxdt = -exp(y)+1/sqrt(1-2*y) 
    dydt = -x                    
    return [dxdt, dydt]

from scipy.integrate import odeint
from numpy import linspace, zeros
initial = [0.001, 0.]       
t = linspace(0, 50.0, 100)  
                                                                 
result = odeint(lv, initial, t, args=(8.0, 1.0, 3.0, 1.0))

import matplotlib.pyplot as plt           

plt.legend()
plt.grid(which='major')
plt.xlabel("Debey length", fontsize=16)
plt.ylabel("Normalised current", fontsize=16)
     
j=zeros(shape=(len(result[:,1]),1))
j = (17.11*exp(result[:,1]))-1.0 

plt.plot (t,j, label="Original", linewidth=3.0)     

from scipy import interpolate

xn = j
yn = t

plt.plot(xn, yn, 'o',label='reversed',linewidth=3.0)
plt.show()

f = interpolate.interp1d(xn, yn)
zero = f(0)
print zero

plt.plot (t-zero,j, label="Shifted", linewidth=3.0)   
plt.title('CURRENT, ORIGINAL, REVERSED, SHIFTED')          
plt.legend()
plt.show()
