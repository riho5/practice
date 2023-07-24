import numpy as np
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt

 # -------------------------------------------------
def lowpass(y,n): #位相はズレる
    Res = np.array([0])
    dt = 0.02
    A = n/(n+dt)
    for yn in y[1:]:
        res = (1-A)*yn+A*Res[-1]
        Res = np.append(Res,res)
    return Res

def get_lowpass(y,n = 0.05):
    return lowpass(y,n)
    
 # -------------------------------------------------
def highpass(y,n):
    Res = np.array([0])
    dt = 0.02

    for yn,yn_1 in zip(y[1:],y[:-1]):
        res = (2*n*(yn-yn_1)+(2*n-dt)*Res[-1])/(2*n+dt)
        Res = np.append(Res,res)
    return Res
    
 # -------------------------------------------------
def complementaryfilter(a,g,n = 0.05):

    # (a : angle [rad], g : gyro [rad/deg], n = default 0.05 (1/20))
    # return -> angle [deg]

    Res = np.array([0])
    dt = 0.02 #timestep
    for an,an_1,gn,gn_1 in zip(a[1:],a[:-1],g[1:],g[:-1]):
        res = (2*n-dt)/(2*n+dt)*Res[-1]+dt/(2*n+dt)*(an+an_1)+dt*n/(2*n+dt)*(gn+gn_1)
        Res = np.append(Res,res)
    
    return np.degrees(Res)
