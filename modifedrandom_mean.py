#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:16:28 2024

@author: isaacthompson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:55:11 2024

@author: isaacthompson
"""

import numpy as np
import matplotlib.pyplot as plt

def random_walks(n, num_walkers):

    positions = np.zeros((num_walkers, n + 1))
    for i in range(1, n + 1):
       
        positions[:, i] = positions[:, i - 1] + np.random.choice([-1, 1], size=num_walkers)
    return positions


n = int(input("Enter the number of steps (positive integer): "))
if n <= 0:
    print("Choose a positive integer.")
    exit()

num_walkers = int(input("Enter a positive integer for the number of walkers: ")) 
if num_walkers <=0:
    print("Choose a postive integer.")
    exit()


positions = random_walks(n, num_walkers)


mean_displacement = np.mean(positions, axis=0)  # <x_n>
mean_squared_displacement = np.mean(positions**2, axis=0)  # <x_n^2>


plt.figure(figsize=(10, 6))
plt.plot(range(n + 1), mean_squared_displacement, label=r"$\langle x_n^2 \rangle$", color="red")
plt.xlabel("Step Number")
plt.ylabel(r"$\langle x_n^2 \rangle$")
plt.title("Mean Squared Displacement vs Step Number")
plt.legend()
plt.grid()
plt.show()