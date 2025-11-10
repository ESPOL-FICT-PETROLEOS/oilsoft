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


#%% Generate random values for porosity - Freddy
# Random values using normal distribution
porosity_norm = norm.rvs(loc=0.4, scale=0.5, size=1000)

# Define minimun values
porosity_norm = np.where(porosity_norm < 0, 0, porosity_norm)

# Define maximum value
porosity_norm = np.where(porosity_norm > 0.4, 0.4, porosity_norm)


# Random values using lognormal distribution
porosity_lognorm = lognorm.rvs(s=0.1, loc=0, scale=0.05, size=1000)

porosity_lognorm = np.where(porosity_lognorm < 0, 0, porosity_lognorm)

porosity_lognorm = np.where(porosity_lognorm > 0.4, 0.4, porosity_lognorm)


# Random values using Exponential distribution
porosity_expon = expon.rvs(loc=0, scale=0.05, size=1000)

porosity_expon = np.where(porosity_expon < 0, 0, porosity_expon)

porosity_expon = np.where(porosity_expon > 0.4, 0.4, porosity_expon)


# Random values using Triangular distribution
porosity_tri = triang.rvs(c=0.3, loc=0, scale= 0.4, size=1000)


# Random values using uniform distribution
porosity_uni = uniform.rvs(loc=0, scale=0.4, size=1000)


print(porosity_expon)

# Visualize distributions
plt.hist(porosity_lognorm, bins=100)
plt.show()


#%% Generate random values for Thickness - Lissette
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


#%% Generate random values for Initial water saturation - César
#Ya estan importadas las librerias por lo tanto pasamos al código.

#Distribución normal
swi_norm = norm.rvs(loc=0.45,  scale=0.15, size=1000)
#Definimos un límite mínimo y máximo (0-1)
swi_norm = np.where(swi_norm < 0, 0, swi_norm)
swi_norm = np.where(swi_norm > 1, 1, swi_norm)

#Repetimos el código para las otras distribuciones

#Distribución lognormal
swi_lognorm = lognorm.rvs(s=0.15, loc=0, scale=0.05, size=1000)
swi_lognorm = np.where(swi_lognorm < 0, 0, swi_lognorm)
swi_lognorm = np.where(swi_lognorm > 1, 1, swi_lognorm)

#Destribución exponencial
swi_expon = expon.rvs(loc= 0, scale= 0.2, size=1000)
swi_expon = np.where(swi_expon < 0, 0, swi_expon)
swi_expon = np.where(swi_expon > 1, 1, swi_expon)

#Distribución triangular
swi_tri = triang.rvs(c=0.3, loc=0.1, scale= 0.9, size=1000)
swi_tri = np.where(swi_tri < 0, 0, swi_tri)
swi_tri = np.where(swi_tri > 1, 1, swi_tri)

#Distribución uniforme
swi_uni = uniform.rvs(loc=0.1 , scale=0.9, size=1000)
swi_uni = np.where(swi_uni < 0, 0, swi_uni)
swi_uni = np.where(swi_uni > 1, 1, swi_uni)

print(swi_expon)

# Visualize distributions
plt.hist(swi_uni, bins=100)
plt.show()

#%% Generate random values for Bo - Marco

# Normal distribution
bo_norm = norm.rvs(loc=1.4, scale=0.5, size=1000)

# Limitar valores (Bo no puede ser negativo)
bo_norm = np.where(bo_norm < 0, 0, bo_norm)


# Lognormal distribution
bo_lognorm = lognorm.rvs(s=0.1, loc=0, scale=1.2, size=1000)


# Exponential distribution
bo_expon = expon.rvs(loc=0, scale=1.2, size=1000)


# Triangular distribution
bo_tri = triang.rvs(c=0.3, loc=1.1, scale=2, size=1000)


# Uniform distribution
bo_uni = uniform.rvs(loc=1.1, scale=2, size=1000)


# Visualización de las distribuciones
fig, axs = plt.subplots(3, 2, figsize=(10, 10))
axs = axs.flatten()

axs[0].hist(bo_norm, bins=50, color='skyblue', edgecolor='black')
axs[0].set_title('Normal Distribution (Bo)')

axs[1].hist(bo_lognorm, bins=50, color='lightgreen', edgecolor='black')
axs[1].set_title('Lognormal Distribution (Bo)')

axs[2].hist(bo_expon, bins=50, color='salmon', edgecolor='black')
axs[2].set_title('Exponential Distribution (Bo)')

axs[3].hist(bo_tri, bins=50, color='plum', edgecolor='black')
axs[3].set_title('Triangular Distribution (Bo)')

axs[4].hist(bo_uni, bins=50, color='khaki', edgecolor='black')
axs[4].set_title('Uniform Distribution (Bo)')

plt.tight_layout()
plt.show()

print("Ejemplo de valores generados:")
print(f"Normal: {bo_norm[:5]}")
print(f"Lognormal: {bo_lognorm[:5]}")
print(f"Exponential: {bo_expon[:5]}")
print(f"Triangular: {bo_tri[:5]}")
print(f"Uniforme: {bo_uni[:5]}")