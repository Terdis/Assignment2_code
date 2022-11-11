import numpy as np

def integrate(function, N, x_min, x_max):
    integral=0.0
    dx=(x_max-x_min)/N
    for i in range(0, N):
        x=(x_min+i+.5)*dx
        dI=function(x)*dx
        integral+=dI

    return integral

def sinIntegral(x_min, x_max):
    N=[10, 100, 1000, 1e4, 1e5, 1e6]

    function=lambda x: np.sin(x)

    results=np.array([integrate(function,  n, x_min, x_max) for n in N])

    return results



