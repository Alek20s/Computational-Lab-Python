m=0
while m<4:
    m=m+1   
    from numpy import linspace, zeros
    vs=zeros(12)
    vs[1]=1.
    vs[2]=1.5
    vs[3]=2.
    
    from scipy import exp, sqrt
    
    def lv(state, time, alpha, beta, gamma, delta):
        
        x = state[0]
        y = state[1]
        dxdt = -exp(y)+vs[m]/sqrt(vs[m]-2*y) 
        dydt = -x                    
        return [dxdt, dydt]
    
    from scipy.integrate import odeint
    
    initial = [0.001, 0.]       
    t = linspace(0, 50.0, 100)  
                                                                    
    result = odeint(lv, initial, t, args=(8.0, 1.0, 3.0, 1.0))
    
    import matplotlib.pyplot as plt           
            
    j=zeros(shape=(len(result[:,1]),1))
    j = (17.11*exp(result[:,1]))-1.0 
    
    from scipy import interpolate
    xn = j
    yn = t
    
    f = interpolate.interp1d(xn, yn)
    zero = f(0)
    
    plt.plot (t-zero,j, label="Vs={var}".format(var=vs[m]), linewidth=3.0)  
    plt.grid(True)
    plt.xlabel("Deybe length", fontsize=20)
    plt.ylabel("Normolised current", fontsize=20)
             
    plt.legend()
    plt.show()