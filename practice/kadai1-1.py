# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:35:10 2022

@author: Private
"""

import numpy as np
import matplotlib.pyplot as plt

def equation(x):
    '''
    Compute (1) y = sin(PI*x).
    '''
    return np.sin(np.pi*x)


def show_graph(x, y, xlim=None, ylim=None, xticks=None, yticks=None):
    '''
    plot 
    '''
    plt.plot(x, y)
    plt.xlim(xlim)
    plt.xticks(xticks)
    plt.ylim(ylim)
    plt.yticks(yticks)
    plt.show()
    pass

if __name__ == "__main__":
    # range(-4PI, 4PI), Hz
    x = ((np.arange(10001, dtype=float)-5000)/5000)*np.pi*4
    y = equation(x)
    show_graph(x, y, xlim=(-4*np.pi, 4*np.pi), ylim=(-1.0, 1.0))
    pass
    
    