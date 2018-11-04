#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:28:56 2018

@author: juandiego
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def buffons_needle(b=1.0, a=1.0, n_runs=1000000):
    n_hits = 0
    for run in range(n_runs):
        x_center = np.random.uniform(0, b/2.0)
        gamma = 2
        while gamma > 1:
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            gamma = np.sqrt(x**2 + y**2)
            if gamma < 1:
                x_tip = x_center - (a/2.0)*x/gamma
                if x_tip < 0:
                    n_hits += 1
    return (a*2.0*n_runs)/(b*n_hits)


def direct_monte_carlo(trials=4000):
    hits = 0
    for trial in range(trials):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if (x**2 + y**2) < 1.0:
            hits+=1
    return 4*hits/trials


def markov_monte_carlo(trials=4000, delta=0.1):
    hits = 0
    x, y = 1.0, 1.0
    for trial in range(trials):
        del_x, del_y = np.random.uniform(-delta, delta), np.random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0:
            hits+=1
    return 4*hits/trials


def multi_run(method, runs=1000):
    for run in range(runs):
        print(method())


def pebble_basic():
    
    neighbors = [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
                 [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
                 [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
    
    t_max = 4
    site = 8
    t = 0
    while t < t_max:
        t += 1
        site = neighbors[site][np.random.randint(4)]
        print(site)
        

def pebble_transfer():
    neighbors = [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
                 [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
                 [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
    
    transfer = np.zeros([9,9])
    
    for k in range(9):
        for neigh in range(4):
            transfer[neighbors[k][neigh], k] += 0.25
    
    eigenvalues, eigenvectors = np.linalg.eig(transfer)
    
    position = np.zeros(9)
    position[8] = 1.0
    
    for t in range(100):
        print (t,' ',['%0.5f' % i for i in position])
        position = np.dot(transfer, position)
    
    print(np.sort(eigenvalues))


def pebble_transfer_sub():
    neighbors = [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
                 [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
                 [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
    
    transfer = np.zeros([9,9])
    
    for k in range(9):
        for neigh in range(4):
            transfer[neighbors[k][neigh], k] += 0.25
    
    eigenvalues, eigenvectors = np.linalg.eig(transfer)
    
    position = np.zeros(9)
    position[8] = 1.0
    
    pos_0 = np.zeros(100)
    
    for t in range(100):
        print(t, ' ', ['%0.5f' % abs(i -(1/9)) for i in position])
        pos_0[t] = position[0]
        position = np.dot(transfer, position)
    
    plt.semilogy(pos_0, np.arange(100), color='orange')
    plt.xlim([0, 100])
    plt.ylim([10**-13, 10**0])
    plt.show()