#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:37:16 2024

@author: isaacthompson
"""
import numpy as np
import matplotlib.pyplot as plt


n = 100

# n <= 0:
   # print("Choose a positive integer.")
   # exit()  



def random_walk(n):
   
    (x,y) = (np.zeros(n + 1), np.zeros(n + 1))  # Start at 0, so we need n+1 elements
    for i in range(1, n + 1):
       
        x[i] = x[i - 1] + np.random.choice([-1, 0, 1])
        y[i] = y[i - 1] + np.random.choice([-1, 0, 1])
        
    return (x, y)


(x, y) = random_walk(n)


plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Random Walk", color="blue")
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.xlabel("Position in x")
plt.ylabel("Position  in y")
plt.title(f"Random Walk with {n} Steps")
plt.legend()
plt.grid()
plt.show()



