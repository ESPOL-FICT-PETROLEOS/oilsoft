#%% Import Pyhton Libraries
from poes.model.poes import poes
import numpy as np
from scipy.stats import norm, lognorm, expon, triang, uniform
import matplotlib.pyplot as plt

#%% Test poes function
area = 20 #acres
h = 15 #ft
poro = 0.30
swi = 0.10
boi = 1.25


Poes = poes(area, h, poro, swi, boi)
print(f"POES is: {Poes:.2f} bbl")


#%% Test array values
area = np.array([20, 30, 40, 50, 60])
h = np.array([10, 20, 30, 40, 50])
poro = np.array([0.30, 0.32, 0.25, 0.45, 0.28])
swi = np.array([0.10, 0.15, 0.25, 0.30, 0.32])
boi = np.array([1.15, 1.25, 1.30, 1.18, 1.51])

Poes_array = np.round(poes(area, h, poro, swi, boi), 2)
print(Poes_array)

#%%Generate random values for Thickness - Lissette
# Generate random values for thickness (h)

# Normal distribution
h_norm = norm.rvs(loc=30, scale=0.5, size=1000)

# Lognormal distribution
h_lognorm = lognorm.rvs(s=0.5, loc=0, scale=30, size=1000)

# Exponential distribution
h_expon = expon.rvs(loc=0, scale=30, size=1000)

# Triangular distribution
h_tri = triang.rvs(c=0.3, loc=10, scale=80, size=1000)

# Uniform distribution
h_uni = uniform.rvs(loc=10, scale=80, size=1000)

#plots
print(h_norm[:10])

plt.hist(h_tri, bins=100, color='skyblue', edgecolor='black')
plt.title("Distribución Triangular - Espesor (h)")
plt.xlabel("Espesor (ft)")
plt.ylabel("Frecuencia")
plt.show()