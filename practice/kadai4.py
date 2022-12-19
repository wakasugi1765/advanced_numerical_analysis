# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 22:32:11 2022

@author: Private
"""

import numpy as np
import matplotlib.pyplot as plt

def step(t):
    '''
    return unit step signal(u(t))
    '''
    return np.where(t<0, 0, 1)

def delta(t):
    '''
    return delta function(δ(t))
    '''
    return np.where(t==0, np.inf, 0)

def equation01(t):
    '''
    x(t) = sin(t)u(t)
    '''
    return np.sin(t)*step(t)

def equation02(t):
    '''
    x(t) = e^(-t)u(t)
    '''
    return np.exp(-t)*step(t)

def equation03(t):
    '''
    x(t) = u(t)-2u(t-2)+u(t-4)
    '''
    return step(t)-2*step(t-2)+step(t-4)

def equation04(t):
    '''
    x(t) = Σ[k=0,∞){u(t-2k)-u(t-2k-1)}
    '''
    k, xt = 0, np.zeros_like(t) 
    while True:
        buf = step(t-2*k)-step(t-2*k-1)
        if buf.sum() == 0:
            break
        k  += 1
        xt += buf
    return xt

def equation05(t):
    a = step(t)-step(t-2)
    b = t*step(t)-2*(t-1)*step(t-1)
    return a*b

def equation06(t):
    return step(t)-2*step(t-1)+step(t-2)

def equation07(t):
    t = 0.5*t+2
    return equation05(t+1)

def equation08(t):
    return step(6-2*t)

def equation09(t):
    return delta(t**2-2*t-3)

def equation10(t):
    return np.exp(-t)*np.sin(t)*step(t)

def show_graph(x,y):
    plt.plot(x,y)
    plt.show()
    pass

if __name__ == '__main__':
    # st, et = -10, 10
    st, et = -10, 10
    t  = np.linspace(st, et, (et-st)*100)
    # t = np.arange(101)-50
    # xt = step(t)
    # xt = equation01(t)
    # xt = equation02(t)
    # xt = equation03(t)
    # xt = equation04(t)
    # xt = equation05(t)
    # xt = equation06(t)
    # xt = equation07(t)
    # xt = equation08(t)
    # xt = equation09(t)
    xt = equation10(t)
    show_graph(t, xt)