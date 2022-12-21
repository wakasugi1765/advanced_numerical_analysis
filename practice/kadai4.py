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

def show_graph(x, y, pi=False):
    fontsize = plt.rcParams["font.size"]
    plt.rcParams["font.size"] = 20
    fig = plt.figure(figsize=(16.0, 9.0), dpi=120) # FulHD(1920*1080)
    #xticks, xticklabels = get_xticks(x)
    if pi:
        xlim = (x[0]-0.1, x[-1]+0.1)
        xticks, xticklabels = get_xticks_pi(x)
    else:
        st, et = int(x[0]), int(x[-1])
        xlim=(st-0.1, et+0.1)
        xticks=np.linspace(st, et, et-st+1)
        xticklabels = xticks
    ylim, yticks = get_ylim(y)
    ax  = fig.add_subplot(
        1,1,1,
        xlabel='t', xlim=xlim, xticks=xticks, xticklabels=xticklabels,
        ylabel='y(t)', ylim=ylim, yticks=yticks
        )
    # ax.legend(fontsize=20)

    plt.plot(x,y)
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.rcParams["font.size"] = fontsize
    pass

def show_delta(*x):
    fontsize = plt.rcParams["font.size"]
    plt.rcParams["font.size"] = 20
    fig = plt.figure(figsize=(16.0, 9.0), dpi=120) # FulHD(1920*1080)
    st, et = -5, 5
    ax  = fig.add_subplot(
        1,1,1,
        xlabel='t', xlim=(st,et), xticks=np.linspace(st, et, et-st+1),
        ylabel='x(t)', ylim=(-0.1,1.1), yticks=[0,1], yticklabels=[0, '∞']
        )
    # ax.legend(fontsize=20)

    # plt.plot(x,y)
    
    for xi in x:
        plt.scatter(xi, 0, marker='o', color='b', s=100)
        plt.scatter(xi, 1, marker='^', color='b', s=100)
        plt.plot([xi,xi], [0,1], color='b')
        
    # plt.plot([1,1], [0,1])
    # plt.plot([2,2], [0,2])
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.rcParams["font.size"] = fontsize
    pass

def get_ylim(y):
    max_val = np.abs(y).max()
    y_max = 0.25

    while max_val >= y_max:
        print(max_val, y_max)
        y_max += 0.25
    ylim = (-y_max-0.1, y_max+0.1)
    yticks = np.linspace(-y_max, y_max, int((2*y_max)/0.25)+1)
    
    return ylim, yticks

def get_xticks_pi(x):
    st, et = x[0], x[-1]
    xticks, xticklabels = [], []
    k = int(np.abs(st)//np.pi)
    for i in range(-k, k+1):
        xticks.append(i*np.pi)
        xticklabels.append('{}π'.format(i))
        pass
    return xticks, xticklabels

if __name__ == '__main__':
    st, et = -10, 10
    t  = np.linspace(st, et, (et-st)*100)
    # xt, pi = equation01(t), True
    # xt, pi = equation02(t), False
    # xt, pi = equation03(t), False
    # xt, pi = equation04(t), False
    # xt, pi = equation05(t), False
    # xt, pi = equation06(t), False
    xt, pi = equation07(t), False
    # xt, pi = equation08(t), False
    # xt = show_delta(1,2)
    # xt, pi = equation10(t), False
    show_graph(t, xt, pi)