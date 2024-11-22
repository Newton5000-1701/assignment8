#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:33:06 2024

@author: isaacthompson
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 70  # mass of the cyclist (kg)
P = 400  # power output (W)
v10 = 4 #initial velocity with linear drag
v20 = 4 #initial velocity with linear and quadratic drag 
V0 = 4 # initial velocity with grav and all drag (m/s)
dt = 0.1  # time step (s)
t_max = 200  # maximum time (s)
n = 2 * 10**(-5) #(Viscosity Pa*s)
A = 0.33 #Surface area
C_D = 0.9 #Drag coefficient
rho = 1.204 #kg/m^3, air density
h = 2 #Height 
g = 9.81 #m/s^2 acceleration due to gravity at sea level
gradient = float(input("Enter a small surface gradient: "))
theta = np.arctan(gradient)

t = np.arange(0, t_max + dt, dt)


v1 = np.zeros_like(t)
v1[0] = v10

v2 = np.zeros_like(t)
v2[0] = v20

V = np.zeros_like(t)
V[0] = V0

for j in range(1, len(t)):
    dv1dt1 = (P / (m * v1[j-1]))  - (n * A * v1[j-1] / (h*m))
    v1[j] = v1[j-1] + dv1dt1 * dt
    


for i in range(1, len(t)):
    dv2dt2 = (P / (m * v2[i-1]))  - (n*A*v2[i-1] / (m*h)) - ((1/(2*m)) * C_D * rho * A * v2[i-1]**2)
    v2[i] = v2[i-1] + dv2dt2 * dt 
    
for k in range(1,len(t)):
    dVdt = (P / (m * V[k-1]))  - (n*A*V[k-1] / (m*h)) - ((1/(2*m)) * C_D * rho * A * V[k-1]**2) - g*np.sin(theta)
    V[k] = V[k-1] + dVdt * dt


# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(t, v1, label='Viscous drag only', color='b')
plt.plot(t, v2, label='Viscous and aerodynamic drag', color='g')
plt.plot(t, V, label='All drag and gravity', color='r')
plt.title("Cyclist's Velocity Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="upper right")
plt.grid(True)
plt.savefig("bicycle.png")
plt.show()
